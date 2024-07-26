# © [2024] Malith-Rukshan. All rights reserved.
# Repository: https://github.com/Malith-Rukshan/Suno-API

from typing import List
from pydantic import BaseModel, ConfigDict

class ModelVersions:
    """Class holding available Suno AI model versions.
    
    Models:
    - CHIRP_V3_5: Newest model, better song structure, max 4 minutes.
    - CHIRP_V3_0: Broad, versatile, max 2 minutes.
    - CHIRP_V2_0: Vintage Suno model, max 1.3 minutes.
    """
    CHIRP_V2_0 = "chirp-v2-0"
    CHIRP_V3_0 = "chirp-v3-0"
    CHIRP_V3_5 = "chirp-v3-5"
    AVAILABLE_MODELS = [CHIRP_V2_0, CHIRP_V3_0, CHIRP_V3_5]

class ClipMetadataHistory(BaseModel):
    id: str | None = None
    type: str | None = None
    infill: bool | None = None
    source: str | None = None
    continue_at: float | None = None

class ClipMetadata(BaseModel):
    tags: str | None = None
    prompt: str | None = None
    gpt_description_prompt: str | None = None
    audio_prompt_id: str | None = None
    history: List[ClipMetadataHistory] | None = None
    concat_history: str | None = None
    stem_from_id: str | None = None
    type: str | None = None
    duration: float | None = None
    refund_credits: float | None = None
    stream: bool | None = None
    infill: bool | None = None
    is_audio_upload_tos_accepted: bool | None = None
    error_type: str | None = None
    error_message: str | None = None

    model_config = ConfigDict(protected_namespaces=())


class Clip(BaseModel):
    id: str
    video_url: str | None = None
    audio_url: str | None = None
    image_url: str | None = None
    image_large_url: str | None = None
    is_video_pending: bool
    major_model_version: str
    model_name: str
    metadata: ClipMetadata
    is_liked: bool
    user_id: str
    display_name: str
    handle: str
    is_handle_updated: bool
    is_trashed: bool
    reaction: dict | None = None
    created_at: str
    status: str
    title: str
    play_count: int | None = None
    upvote_count: int | None = None
    is_public: bool

    class Config:
        protected_namespaces = ()
        json_schema_extra = {
            "example": {
                "id": "aaaaaaaa-aaaa-aaaa-aaaaaaaaaaaaa",
                "video_url": "https://cdn1.suno.ai/aaaaaaaa-aaaa-aaaa-aaaaaaaaaaaaa.mp4",
                "audio_url": "https://cdn1.suno.ai/aaaaaaaa-aaaa-aaaa-aaaaaaaaaaaaa.mp3",
                "image_url": "https://cdn2.suno.ai/image_aaaaaaaa-aaaa-aaaa-aaaaaaaaaaaaa.jpeg",
                "image_large_url": "https://cdn2.suno.ai/image_large_aaaaaaaa-aaaa-aaaa-aaaaaaaaaaaaa.jpeg",
                "is_video_pending": False,
                "major_model_version": "v3.5",
                "model_name": "chirp-v3",
                "metadata": {
                    "tags": "chuu chuu chuu, groovy, funky, pop, upbeat, funk, progressive",
                    "prompt": "",
                    "gpt_description_prompt": None,
                    "audio_prompt_id": "aaaaaaaa-aaaa-aaaa-aaaaaaaaaaaaa",
                    "history": [
                    {
                        "id": "aaaaaaaa-aaaa-aaaa-aaaaaaaaaaaaa",
                        "type": "upload",
                        "infill": False,
                        "source": "web",
                        "continue_at": 46.83755102040816
                    },
                    {
                        "id": "aaaaaaaa-aaaa-aaaa-aaaaaaaaaaaaa",
                        "type": "gen",
                        "infill": False,
                        "source": "web",
                        "continue_at": 192.96
                    }
                    ],
                    "concat_history": None,
                    "stem_from_id": None,
                    "type": "gen",
                    "duration": 12.34,
                    "refund_credits": False,
                    "stream": True,
                    "infill": False,
                    "has_vocal": False,
                    "is_audio_upload_tos_accepted": True,
                    "error_type": None,
                    "error_message": None
                },
                "is_liked": True,
                "user_id": "aaaaaaa-aaaa-aaaa-aaaaaaaaaaaaaaa",
                "display_name": "demo",
                "handle": "demo",
                "is_handle_updated": False,
                "avatar_image_url": "https://cdn1.suno.ai/defaultPink.webp",
                "is_trashed": False,
                "reaction": {
                    "clip": None,
                    "play_count": 7,
                    "skip_count": 0,
                    "flagged": False,
                    "flagged_reason": None,
                    "feedback_reason": None,
                    "reaction_type": None,
                    "updated_at": "2099-08-01T12:00:00.000Z"
                },
                "created_at": "2099-08-01T10:00:00.000Z",
                "status": "complete",
                "title": "demo",
                "play_count": 7,
                "upvote_count": 0,
                "is_public": False
            }
        }


class RequestParams(BaseModel):
    model_version: str = ModelVersions.CHIRP_V3_5
    prompt: str
    is_custom: bool = False
    tags: str = ""
    title: str = ""
    make_instrumental: bool = False
    wait_audio: bool = False

    class Config:
        protected_namespaces = ()
        json_schema_extra = {"examples": [{
            "model_version" : "chirp-v3-5",
            "prompt": "I found a love, for me\nDarling, just dive right in and follow my lead\nWell, I found a girl, beautiful and sweet\nOh, I never knew you were the someone waiting for me\n\n′Cause we were just kids when we fell in love\nNot knowing what it was\nI will not give you up this time\nBut darling, just kiss me slow\nYour heart is all I own\nAnd in your eyes, you're holding mine\n\nBaby, I′m dancing in the dark\nWith you between my arms\nBarefoot on the grass\nListening to our favourite song\nWhen you said you looked a mess\nI whispered underneath my breath\nBut you heard it\nDarling, you look perfect tonight",
            "is_custom": True,
            "tags": "English men voice",
            "title": "Perfect by Malith-Rukshan/Suno-API",
            "make_instrumental": False,
            "wait_audio": True
        }]}


class CreditsInfo(BaseModel):
    credits_left: int
    period: int | None = None
    monthly_limit: int
    monthly_usage: int

    class Config:
        protected_namespaces = ()
        json_schema_extra = {
            "example": {
                "credits_left": 50,
                "period": "Date-Here",
                "monthly_limit": 50,
                "monthly_usage": 0
            }
        }
