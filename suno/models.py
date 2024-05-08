# © [2024] Malith-Rukshan. All rights reserved.
# Repository: https://github.com/Malith-Rukshan/Suno-API


from pydantic import BaseModel, ConfigDict

class ClipMetadata(BaseModel):
    tags: str | None = None
    prompt: str | None = None
    gpt_description_prompt: str | None = None
    audio_prompt_id: str | None = None
    history: str | None = None
    concat_history: str | None = None
    type: str | None = None
    duration: float | None = None
    refund_credits: float | None = None
    stream: bool | None = None
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
                "id": "124b735f-7fb0-42b9-8b35-761aed65a7f6",
                "video_url": "",
                "audio_url": "https://audiopipe.suno.ai/?item_id=124b735f-7fb0-42b9-8b35-761aed65a7f6",
                "image_url": "https://cdn1.suno.ai/image_124b735f-7fb0-42b9-8b35-761aed65a7f6.png",
                "image_large_url": "https://cdn1.suno.ai/image_large_124b735f-7fb0-42b9-8b35-761aed65a7f6.png",
                "is_video_pending": False,
                "major_model_version": "v3",
                "model_name": "chirp-v3",
                "metadata": {
                    "tags": "English men voice",
                    "prompt": "I found a love, for me\nDarling, just dive right in and follow my lead\nWell, I found a girl, beautiful and sweet\nOh, I never knew you were the someone waiting for me\n\n′Cause we were just kids when we fell in love\nNot knowing what it was\nI will not give you up this time\nBut darling, just kiss me slow\nYour heart is all I own\nAnd in your eyes, you're holding mine\n\nBaby, I′m dancing in the dark\nWith you between my arms\nBarefoot on the grass\nListening to our favourite song\nWhen you said you looked a mess\nI whispered underneath my breath\nBut you heard it\nDarling, you look perfect tonight",
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
                "user_id": "2340653f-32cb-4343-artb-09203ty749e9",
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
        }


class RequestParams(BaseModel):
    prompt: str
    is_custom: bool = False
    tags: str = ""
    title: str = ""
    make_instrumental: bool = False
    wait_audio: bool = False

    class Config:
        protected_namespaces = ()
        json_schema_extra = {"examples": [{
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
