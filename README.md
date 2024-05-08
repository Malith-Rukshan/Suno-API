<p style="text-align:center;" align="center">
  <img align="center" src="https://raw.githubusercontent.com/Malith-Rukshan/Suno-API/main/Logo.png" width="300px" height="300px"/>
</p>
<h1 align="center">✨ Suno AI API 🎵</h1>
<div align='center'>

[![PyPI Package](https://img.shields.io/badge/PyPi-Library-1cd760?logo=pypi&style=flat)](https://pypi.org/project/SunoAI/)
[![Updates Telegram Channel](https://img.shields.io/badge/Updates-@SunoAPI-blue?logo=telegram&style=flat)](https://t.me/SunoAPI)

</div>
<h4 align="center">✨ Python API Library for Suno AI — Create Music with Generative AI ! 🚀</h4>
<div align="center">
  - Available as Both Python Library and REST API -
  <br />
  <br />
  <a href="https://pypi.org/project/SunoAI/">Python Library</a>
  ·
  <a href="https://github.com/Malith-Rukshan/Suno-API/issues/new">Update Channel</a>
</div>
</br>

**📚 SunoAI API Library is an unofficial Python client for interacting with [Suno AI](https://suno.ai/)'s music generator**. This library facilitates generating music using Suno's Chirp v3 model and includes main functions of Suno AI with a built-in music downloader. It can be deployed as a **[REST API](#-deployment---rest-api)** using FastAPI, Local, Docker, on a PaaS provider like Heroku.

## ✨ Features
- **Python Client 🐍**: Easily interact with Suno AI.
- **Song Generation 🎶**: Utilize the Chirp v3 model for generating music.
- **Retrieve Song Info by ID 🎵**: Access detailed information about any song on Suno AI.
- **Music Downloader 📥**: Built-in functionality to download any music on Suno AI directly.
- **REST API Deployment 🌐**: Deployable as a REST API on PasS Platform , VPS or Local.
- **Comprehensive Documentation 📚**: Includes detailed examples and usage guides.
- **Docker Support 🐳**: Enables containerized deployment with Docker for flexibility.
- **PaaS Deployment ☁️:** Facilitates deployment on platforms like Heroku for convenient accessibility.

# 🏷 Prerequisites
 📋 Before using the library or REST API, <b>you must sign up on the [suno.ai](https://app.suno.ai/) website and obtain your cookie</b> as shown in this screenshot.

💡 You can find cookie from the Web Browser's **Developer Tools -> Network Tab**

<details>
    <summary>Click to view - Screenshot</summary>
<img src="https://raw.githubusercontent.com/Malith-Rukshan/Suno-API/main/Screenshot.jpg" alt="How to get Cookie from Suno.AI">

Just right click & open Inspect. Filter : `_clerk_js_version`
</details>
</br>

Set this cookie as `SUNO_COOKIE` environment variable or initialize the library as shown below.

```
import suno
client = suno.Suno(cookie='YOUR_COOKIE_HERE')
```

## 💾 Installation
Install the library using pip: 

```
pip install SunoAI
```

<a href='https://pypi.org/project/SunoAI/'>
<img src='https://img.shields.io/badge/PyPi-Library-1cd760?logo=pypi&style=flat'>
</a>

## 🚀 Deployment - REST API

### Deploy on PasS

Set `SUNO_COOKIE` as an Environmental variable before deploy. -  [Instructions](#-prerequisites)

[![Deploy with heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/Malith-Rukshan/Suno-API)

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)
</br>

### Deploy on Local or VPS

```
export SUNO_COOKIE="YOUR_COOKIE_HERE"
git clone git@github.com:Malith-Rukshan/Suno-API.git
pip3 install -r requirements.txt
cd Suno-API
fastapi run api.py --port 8080
```
🔗 Available at : http://127.0.0.1:8080

## 🛠️ Usage

**⚡️ Quick Start :**
```
import suno
client = suno.Suno(cookie='YOUR_COOKIE_HERE')

# Generate a song
song = client.generate(prompt="A serene landscape", wait_audio=True)

# Download generated song
file_path = client.download(song=song)
print(f"Song downloaded to: {file_path}")
```

### 📚 Library Methods

`generate()`
- <b>Arguments</b>:
  - prompt (str): Description or lyrics for the song.
  - is_custom (bool): Determines whether to use custom lyrics (True) or a description (False).
  - tags (Optional[str]): Describes desired voice type or characteristics.
  - title (Optional[str]): Title for the generated music.
  - make_instrumental (Optional[bool]): Generates an instrumental version if True.
  - wait_audio (bool): Waits until the audio URLs are ready if True.
- <b>Returns</b>: A list of `Clip` objects containing song data with IDs.
- <b>Example:</b>
  - **By Description**
    ```
    clips = client.generate(
      prompt="A peaceful melody reflecting a serene landscape",
      is_custom=False,
      wait_audio=True
    )
    print(clips)
    ```
  - **By Lyrics - Custom**
    ```
    clips = client.generate(
      prompt="I found a love, for me\nDarling, just dive right in and follow my lead\nWell, I found a girl, beautiful and sweet\nOh, I never knew you were the someone waiting for me...",
      tags="English men voice",
      title="Perfect by Malith-Rukshan/Suno-API",
      make_instrumental= False,
      is_custom=True,
      wait_audio=True
    )
    print(clips)
    ```
**✍️ Usage Note :**
  - When setting `is_custom` to `True`, ensure that the prompt parameter contains the lyrics of the song you wish to generate. Conversely, if `is_custom` is set to `False`, provide a descriptive prompt detailing the essence of the song you want.
  - When `wait_audio` is set to **True**, the request will take longer as it waits for the audio URLs to be ready. If not set, the response will return without `audio_url` but with audio IDs. In such cases, you'll need to call the **get_songs** or **get_song** method after a short interval to retrieve the response with the `audio_url` included, once the generation process is complete.

`get_songs()`
- <b>Arguments</b>:
  - <b>song_ids</b> (Optional[str]): A list of song IDs to fetch specific songs.
- <b>Returns</b>: A list of `Clip` objects representing the retrieved songs.
- Example:
    ```
    songs = client.get_songs(song_ids="123,456")
    print(songs)
    ```

`get_credits()`
- Returns: Current billing and credits information as a `CreditsInfo` object.
- Example:
    ```
    credits_info = client.get_credits()
    print(credits_info)
    ```

`download()`
- Arguments:
  - song (str | Clip): The song to be downloaded. This can be either the ID of the song as a string or a Clip object containing the song's metadata.
  - path (str): The directory path where the song will be saved. If not specified, defaults to "./downloads".
- Returns: str - The full filepath to the downloaded song.
- Raises:
  - TypeError: If the song argument is neither a string ID nor a Clip object.
  - Exception: If the download fails due to issues like an invalid URL or network errors.
- Example:
    ```
    # Using a song ID
    file_path = client.download(song="uuid-type-songid-1234")
    print(f"Song downloaded to: {file_path}")

    # Using a Clip object
    clip = client.get_song("uuid-type-songid-1234")
    file_path = client.download(song=clip)
    print(f"Song downloaded to: {file_path}")
    ```

### 📚 Library Responses

- **Clip Model:**

    The **Clip** class encapsulates the details of a music track generated by the Suno AI. Each attribute of this class provides specific information about the track:
  - **id** (str): Unique identifier for the clip.
  - **video_url** (str): URL of the video version of the song, if available.
  - **audio_url** (str): URL where the audio track can be streamed or downloaded.
  - **image_url** (str): URL of the song's image cover.
  - **image_large_url** (str): URL of a larger version of the song's image cover.
  - **is_video_pending** (bool): Indicates whether the video for the song is still processing.
  - **major_model_version** (str): The major version of the model used to generate the song.
  - **model_name** (str): Name of the model used to generate the track.
  - **metadata** (ClipMetadata): Additional metadata related to the clip including tags, prompts, and other information.
  - **is_liked** (bool): Indicates whether the song has been liked by the user.
  - **user_id** (str): User ID of the person who created or requested the song.
  - **display_name** (str): Display name of the user associated with the song.
  - **handle** (str): User's handle or username.
  - **is_handle_updated** (bool): Specifies whether the user's handle has been updated.
  - **is_trashed** (bool): Indicates if the clip has been marked as trashed.
  - **reaction** (dict): Reactions to the song from users, if any.
  - **created_at** (str): Timestamp indicating when the song was created.
  - **status** (str): Current status of the song (e.g., processing, completed).
  - **title** (str): Title of the song.
  - **play_count** (int): How many times the song has been played.
  - **upvote_count** (int): Number of upvotes the song has received.
  - **is_public** (bool): Indicates whether the song is publicly accessible.

- **CreditsInfo Model:**

    The **CreditsInfo** class provides information about the user's credit balance and usage within the Suno AI system.
  - **credits_left** (int): The number of credits remaining for the user.
  - **period** (int): The current billing period for the credits, represented in some form of date or timeframe.
  - **monthly_limit** (int): The total number of credits allocated to the user for the current month.
  - **monthly_usage** (int): The amount of credits used by the user during the current month.

## 🌐 REST API Usage

**1. Generate Music**

`POST /generate`

  - **Request Body:**
    ```
    {
      "prompt": "A serene melody about the ocean",
      "is_custom": false,
      "tags": "relaxing, instrumental",
      "title": "Ocean Waves",
      "make_instrumental": true,
      "wait_audio": true
    }
    ```

  - **Response:**
    <details>
    <summary>Click to view</summary>
    
    ```
    [
        {
            "id": "124b735f-7fb0-42b9-8b35-761aed65a7f6",
            "video_url": "",
            "audio_url": "https://audiopipe.suno.ai/item_id=124b735f-7fb0-42b9-8b35-761aed65a7f6",
            "image_url": "https://cdn1.suno.aiimage_124b735f-7fb0-42b9-8b35-761aed65a7f6.png",
            "image_large_url": "https://cdn1.suno.aiimage_large_124b735f-7fb0-42b9-8b35-761aed65a7f.png",
            "is_video_pending": False,
            "major_model_version": "v3",
            "model_name": "chirp-v3",
            "metadata": {
                "tags": "English men voice",
                "prompt": "I found a love, for me\nDarling,just dive right in and follow mylead\nWell, I found a girl, beautiful andsweet\nOh, I never knew you were thesomeone waiting for me\n\n′Cause we werejust kids when we fell in love\nNot knowingwhat it was\nI will not give you up thistime\nBut darling, just kiss me slow\nYourheart is all I own\nAnd in your eyes,you're holding mine\n\nBaby, I′m dancing inthe dark\nWith you between myarms\nBarefoot on the grass\nListening toour favourite song\nWhen you said youlooked a mess\nI whispered underneath mybreath\nBut you heard it\nDarling, you lookperfect tonight",
                "gpt_description_prompt": None,
                "audio_prompt_id": None,
                "history": None,
                "concat_history": None,
                "type": "gen",
                "duration": None,
                "refund_credits": None,
                "stream": True,
                "error_type": None,
                "error_message": None
            },
            "is_liked": False,
            "user_id":"2340653f-32cb-4343-artb-09203ty749e9",
            "display_name": "Snonymous",
            "handle": "anonymous",
            "is_handle_updated": False,
            "is_trashed": False,
            "reaction": None,
            "created_at": "2024-05-05T11:54:09.356Z",
            "status": "streaming",
            "title": "Perfect by Malith-Rukshan/Suno-API",
            "play_count": 0,
            "upvote_count": 0,
            "is_public": False
        }
    ]
    ```
    </details>

**2. Retrieve Songs**

`POST /songs`

  - **Request Body:**
    ```
    {
      "song_ids": "uuid-format-1234,4567-abcd"
    }
    ```
  - **Response:**
    Array of Clips - Same to `/generate` Response

**3. Get a Specific Song**

`POST /get_song`

  - **Request Body:**
    ```
    {
      "song_id": "uuid-song-id"
    }
    ```
  - **Response:**
    Just Clip Response - Same to `/generate` Response but Only Clip

**4. Retrieve Credit Information**

`GET /credits`

  - **Response:**
    ```
    {
      "credits_left": 50,
      "period": "2024-05",
      "monthly_limit": 100,
      "monthly_usage": 25
    }
    ```
> According to [Suno.ai](https://suno.ai/) Each song generation consumes 5 credits, thus a total of 10 credits is necessary for each successful call.


## 🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

## 🎯 Credits and Other
All content and music generated through this library are credited to [Suno AI](https://suno.ai/). This unofficial API provides a convenient way to interact with Suno AI's services but does not claim any ownership or rights over the music generated. Please respect  the terms of service of Suno AI when using their platform ❤️.

> This library is intended primarily for educational and development purposes. It aims to enhance and simplify access to Suno AI's music generation capabilities. If you enjoy the music generated, consider supporting Suno AI directly.
> Logo Credit : [@rejaul43](https://dribbble.com/rejaul43)

## ⚖️ License
This project is distributed under the MIT License. This license allows everyone to use, modify, and redistribute the code. However, it comes with no warranties regarding its functionality. For more details, see the [LICENSE](https://github.com/Malith-Rukshan/Suno-API/blob/main/LICENSE) file in the repository.

## 🌟 Support and Community
If you found this project helpful, **don't forget to give it a ⭐ on GitHub.** This helps others find and use the project too! 🫶

Join our Telegram channels, 

- [@SingleDevelopers](https://t.me/SingleDevelopers), for more amazing projects and updates ✓
- [@SunoAPI](https://t.me/SunoAPI), for this project updates ✓

## 📬 Contact
If you have any questions, feedback, or just want to say hi, you can reach out to me:

- Developer : [@MalithRukshan](https://t.me/MalithRukshan)
- Support Group : [@Suno_API](https://t.me/Suno_API)

🧑‍💻 Built with 💖 by [Single Developers </> ](https://t.me/SingleDevelopers)





