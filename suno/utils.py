# © [2024] Malith-Rukshan. All rights reserved.
# Repository: https://github.com/Malith-Rukshan/Suno-API

from .models import Clip, ClipMetadata
from typing import List
import random

os_systems = [
    'Windows NT 10.0; Win64; x64',
    'Windows NT 6.1; WOW64',
    'Macintosh; Intel Mac OS X 10_15_7',
    'Linux x86_64'
]

browsers = [
    'Chrome/103.0.0.0 Safari/537.36',
    'Firefox/102.0',
    'Edge/103.0.1264.37',
    'Opera/9.80 (X11; Linux x86_64) Presto/2.12.388 Version/12.16'
]


def generate_fake_useragent():
    os_system = random.choice(os_systems)
    browser = random.choice(browsers)
    return f'Mozilla/5.0 ({os_system}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}'


def create_clip_from_data(clip_data) -> Clip:
    metadata = ClipMetadata(**clip_data['metadata'])
    clip_data['metadata'] = metadata
    clip_instance = Clip(**clip_data)

    return clip_instance


def response_to_clips(clips_data) -> List[Clip]:
    clips = []
    for clip_data in clips_data:
        clip_instance = create_clip_from_data(clip_data)
        clips.append(clip_instance)

    return clips
