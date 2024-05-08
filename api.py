# © [2024] Malith-Rukshan. All rights reserved.
# Repository: https://github.com/Malith-Rukshan/Suno-API

import os
from typing import List
from suno import suno
from suno.models import RequestParams, CreditsInfo, Clip
import fastapi
from fastapi.responses import RedirectResponse, JSONResponse
from suno import __version__

COOKIE = os.getenv("SUNO_COOKIE")

# Initilize Suno API Client
client = suno.Suno(cookie=COOKIE)

description = """
### Suno AI Unofficial API

<a href='https://pypi.org/project/SunoAI/'>
<img src='https://img.shields.io/badge/PyPi-Library-1cd760?logo=pypi&style=flat'>
</a>
<a href='https://github.com/Malith-Rukshan/Suno-API'>
<img src='https://img.shields.io/badge/Github-Suno--API-blue?logo=github&style=flat'> 
</a>
<a href='https://t.me/SingleDevelopers'>
<img src='https://img.shields.io/badge/Telegram-@SingleDevelopers-blue?logo=telegram&style=flat'> 
</a>

This is an **unofficial API for [Suno AI](https://www.suno.ai/)**, a platform that utilizes artificial intelligence to generate music.

### 🚀 Main Features
- **Generate Music:** Leverage Suno AI's capabilities to create music based on different styles and inputs.
- **Retrieve Music Data:** Access details about generated music tracks, including audio files, metadata, and more.
- **Get Credit Balance Info**
- **Documentation:** [📚 Redoc](/redoc) | [🏷 Usage](https://github.com/Malith-Rukshan/Suno-API?tab=readme-ov-file#-rest-api-usage)

### Repository
You can find the source code for this API at [GitHub](https://github.com/Malith-Rukshan/Suno-API).

### Disclaimer
This API is not officially associated with Suno AI. It was developed to facilitate easier access and manipulation of the music generation capabilities provided by Suno AI's official website.

### Usage
Please note that this API is intended for educational and development purposes. Ensure you respect Suno AI's terms of service when using their services.
"""

# FastAPI app
app = fastapi.FastAPI(
    title="Suno API",
    summary="An Unofficial Python Library for Suno AI API",
    description=description,
    version=__version__,
    contact={
        "name": "Malith Rukshan",
        "url": "https://MalithRukshan.t.me",
        "email": "singledeveloper.lk@gmail.com",
    }
)

# Redirect to Docs :)


@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url='/docs')


@app.post(f"/generate", response_model=List[Clip])
def generate(params: RequestParams) -> JSONResponse:
    clips = client.generate(**params.model_dump())
    return JSONResponse(content=[clip.model_dump() for clip in clips])


@app.post(f"/songs", response_model=List[Clip])
def generate(song_ids: str | None = None) -> JSONResponse:
    clips = client.get_songs(song_ids)
    return JSONResponse(content=[clip.model_dump() for clip in clips])


@app.post(f"/get_song", response_model=Clip)
def generate(song_id: str) -> JSONResponse:
    clip = client.get_song(song_id)
    return JSONResponse(content=clip.model_dump())


@app.get(f"/credits", response_model=CreditsInfo)
def credits() -> JSONResponse:
    credits = client.get_credits()
    return JSONResponse(content=credits.model_dump())
