# © [2024] Malith-Rukshan. All rights reserved.
# Repository: https://github.com/Malith-Rukshan/Suno-API

import os
import pathlib
import random
import time
import logging
from typing import List, Optional
import requests

from .models import Clip, CreditsInfo
from .utils import create_clip_from_data, response_to_clips, generate_fake_useragent

# Setup basic logging configuration
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Fetch the cookie from environment variables; used for authentication
COOKIE = os.getenv("SUNO_COOKIE", "")


class Suno():
    """Main class for interacting with Suno API."""
    BASE_URL = 'https://studio-api.suno.ai'
    CLERK_BASE_URL = 'https://clerk.suno.com'

    def __init__(self, cookie: Optional[str] = None) -> None:
        """Initialize the Suno client with optional cookie. If no cookie is provided, it uses the one from the environment."""
        if cookie is None:
            cookie = COOKIE
        if cookie == "":
            raise Exception("Environment variable SUNO_COOKIE is not found !")

        headers = {
            # Generate a random User-agent for requests
            'User-Agent': generate_fake_useragent(),
            'Cookie': cookie
        }
        self.client = requests.Session()
        self.client.headers.update(headers)
        self.current_token = None
        self.sid = None

        self._get_session_id()  # Retrieve session ID upon initialization
        self._keep_alive()      # Keep session alive

    def _get_session_id(self) -> None:
        """Retrieve a session ID from the Suno service."""
        url = f"{Suno.CLERK_BASE_URL}/v1/client?_clerk_js_version=4.72.1"
        response = self.client.get(url)
        if not response.json()['response']:
            raise Exception(
                "Failed to get session id, you may need to update the SUNO_COOKIE")
        if 'last_active_session_id' in response.json()['response']:
            self.sid = response.json()['response']['last_active_session_id']
        else:
            raise Exception(
                f"Failed to get Session ID: {response.status_code}")

    def _keep_alive(self, is_wait=False) -> None:
        """Renew the authentication token periodically to keep the session active."""
        if not self.sid:
            raise Exception("Session ID is not set. Cannot renew token.")

        renew_url = f"{Suno.CLERK_BASE_URL}/v1/client/sessions/{self.sid}/tokens?_clerk_js_version=4.72.0-snapshot.vc141245"
        renew_response = self.client.post(renew_url)
        logger.info("Renew Token ♻️")

        if is_wait:
            # Sleep randomly to mimic human interaction
            time.sleep(random.uniform(1, 2))

        new_token = renew_response.json()['jwt']
        self.current_token = new_token
        # Set New Token to Headers
        self.client.headers['Authorization'] = f"Bearer {new_token}"

    # Generate Songs
    def generate(self, prompt, is_custom, tags=None, title=None, make_instrumental=False, wait_audio=False) -> List[Clip]:
        """
        Generate songs based on the provided parameters and optionally wait for the audio to be ready.

        Parameters:
        - prompt (str): If is_custom=True, this should be the lyrics of the song. If False, it should be a brief description of what the song should be about.
        - is_custom (bool): Determines whether the song should be generated from custom lyrics (True) or from a description (False).
        - tags (Optional[str]): Describes the desired voice type or characteristics (e.g., "English male voice"). Default is None.
        - title (Optional[str]): The title for the generated music. Default is None.
        - make_instrumental (Optional[bool]): If True, generates an instrumental version of the track. Default is False.
        - wait_audio (bool): If True, waits until the audio URLs are ready and returns them. If False, returns the IDs of the songs being processed, which can be used to fetch the songs later using get_song.

        Returns:
        List[Clip]: A list of Clip objects containing either song IDs or complete song data, depending on the 'wait_audio' parameter.
        """
        self._keep_alive()
        logger.info("Generating Audio...")
        payload = {
            "make_instrumental": make_instrumental,
            "mv": "chirp-v3-0",
            "prompt": ""
        }
        if is_custom:
            payload["tags"] = tags
            payload["title"] = title
            payload["prompt"] = prompt
        else:
            payload["gpt_description_prompt"] = prompt

        response = self.client.post(
            f"{Suno.BASE_URL}/api/generate/v2/", json=payload)

        if response.status_code != 200:
            logger.info("Audio Generate Failed ⁉️")
            raise Exception(f"Error response: {response.text}")

        song_ids = [audio['id'] for audio in response.json()['clips']]
        if wait_audio:
            return self._wait_for_audio(song_ids)
        else:
            self._keep_alive(True)
            logger.info("Generated Audio Successfully ✅")
            return response_to_clips(response.json()['clips'])

    def _wait_for_audio(self, song_ids):
        """Helper method to wait for audio processing to complete."""
        start_time = time.time()
        last_clips = []
        while time.time() - start_time < 100:  # Timeout after 100 seconds
            clips = self.get_songs(song_ids)
            all_completed = all(
                audio.status in ['streaming', 'complete'] for audio in clips)
            if all_completed:
                logger.info("Generated Audio Successfully ✅")
                return clips
            last_clips = clips
            time.sleep(random.uniform(3, 6))  # Wait with variation
            self._keep_alive(True)
        logger.info("Generated Audio Successfully ✅")
        return last_clips

    def get_songs(self, song_ids: str = None) -> List[Clip]:
        """
        Retrieve songs from the library. If song IDs are provided, fetches specific songs; otherwise, retrieves a general list of songs.

        Parameters:
        - song_ids (str): A list of song IDs to retrieve specific songs. If None, the function fetches a general list of songs from the library. Split by ",".

        Returns:
        List[Clip]: A list of Clip objects representing the songs. Each Clip contains detailed information such as song status, URL, and metadata.

        Example:
        - To retrieve specific songs: get_songs(song_ids=["123-abcd-456", "456-cdef-789"])
        - To retrieve a list of all songs in the library: get_songs()
        """
        self._keep_alive()  # Ensure session is active
        url = f"{Suno.BASE_URL}/api/feed/"
        if song_ids:
            url += f"?ids={song_ids}"
        logger.info("Getting Songs Info...")
        response = self.client.get(url)  # Call API
        return response_to_clips(response.json())

    def get_song(self, id: str) -> Clip:
        """
        Retrieve a single song by its ID.

        Parameters:
        - id (str): The ID of the song to retrieve.

        Returns:
        Clip: A Clip object containing details about the song, such as the audio URL, song status, and other metadata.
        """
        self._keep_alive()  # Ensure session is active
        logger.info("Getting Song Info...")
        response = self.client.get(
            f"{Suno.BASE_URL}/api/feed/?ids={id}")  # Call API
        return create_clip_from_data(response.json()[0])

    def get_credits(self) -> CreditsInfo:
        """Retrieve current billing and credits information."""
        self._keep_alive()  # Ensure session is active
        logger.info("Credits Info...")
        response = self.client.get(
            f"{Suno.BASE_URL}/api/billing/info/")  # Call API
        if response.status_code == 200:
            data = response.json()
            result = {
                "credits_left": data["total_credits_left"],
                "period": data["period"],
                "monthly_limit": data["monthly_limit"],
                "monthly_usage": data["monthly_usage"],
            }
            return CreditsInfo(**result)
        else:
            raise Exception(f"Error retrieving credits: {response.text}")

    def _get_dl_path(self, id: str, path: str) -> str:
        output_dir = pathlib.Path(path)
        output_dir.mkdir(parents=True, exist_ok=True)
        return output_dir / f"SunoMusic-{id}.mp3"

    def download(self, song: str | Clip, path: str = "./downloads",) -> str:
        """
        Downloads a Suno song to a specified location.

        Args:
            song (str | Clip): Either the ID of the song or a Clip object representing the song.
            path (str): The directory where the song should be saved. Defaults to "./downloads".

        Returns:
            str: The full filepath of the downloaded song.

        Raises:
            TypeError: If the 'song' argument is not of type str or Clip.
            Exception: If the download fails (e.g., bad URL, HTTP errors).
        """
        if isinstance(song, Clip):
            id = song.id
            url = song.audio_url
        elif isinstance(song, str):
            id = song
            url = self.get_song(id).audio_url
        else:
            raise TypeError
        logger.info(f"Audio URL : {url}")
        response = requests.get(url)
        if not response.ok:
            raise Exception(
                f"failed to download from audio url: {response.status_code}"
            )
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check for HTTP errors
        filename = self._get_dl_path(id, path)
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:  # Filter out keep-alive chunks
                    f.write(chunk)
        logger.info(f"Download complete: {filename}")
        return filename
