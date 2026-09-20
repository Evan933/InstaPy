"""Generate a video with Higgsfield's Seedance 2.5 text-to-video model.

Credentials are read at runtime from HF_KEY (format: key-id:key-secret), which
is loaded from .env.local and never printed. Run with:

    python main.py
"""

import os
import sys

import httpx
from dotenv import load_dotenv

import higgsfield_client

MODEL = 'bytedance/seedance-2.5/text-to-video'

ARGUMENTS = {
    'prompt': 'A cinematic scene at sunset',
    'duration': 5,
    'resolution': '720p',
    'aspect_ratio': '16:9',
}

# subscribe() returns the final payload for terminal states rather than raising,
# so an unsuccessful generation has to be detected from the status field.
UNSUCCESSFUL_STATUSES = {
    'failed': 'the generation failed',
    'canceled': 'the request was canceled',
    'nsfw': 'the request was rejected by content moderation',
}


def find_video_url(payload):
    """Pull the video URL out of the completed request payload."""
    results = payload.get('results') or payload
    if isinstance(results, dict):
        for key in ('video', 'raw', 'min'):
            entry = results.get(key)
            if isinstance(entry, dict) and entry.get('url'):
                return entry['url']
            if isinstance(entry, str) and entry.startswith('http'):
                return entry
        videos = results.get('videos')
        if isinstance(videos, list) and videos:
            first = videos[0]
            return first.get('url') if isinstance(first, dict) else first
        if results.get('url'):
            return results['url']
    return None


def main():
    load_dotenv('.env.local')

    if not os.getenv('HF_KEY') and not (
        os.getenv('HF_API_KEY') and os.getenv('HF_API_SECRET')
    ):
        sys.exit(
            'HF_KEY is not set. Add it to .env.local in key-id:key-secret format.'
        )

    print(f'Submitting {MODEL}...')

    try:
        result = higgsfield_client.subscribe(
            MODEL,
            arguments=ARGUMENTS,
            on_enqueue=lambda request_id: print(f'Queued as {request_id}'),
            on_queue_update=lambda status: print(f'Status: {type(status).__name__}'),
        )
    except higgsfield_client.HiggsfieldClientError as error:
        sys.exit(f'Higgsfield API error: {error}')
    except httpx.HTTPError as error:
        sys.exit(f'Could not reach the Higgsfield API: {error}')

    status = result.get('status')

    if status in UNSUCCESSFUL_STATUSES:
        sys.exit(f'No video was generated: {UNSUCCESSFUL_STATUSES[status]}.')

    if status != 'completed':
        sys.exit(f'No video was generated: unexpected status {status!r}.')

    video_url = find_video_url(result)

    if not video_url:
        sys.exit(f'Request completed but no video URL was found in: {result}')

    print(f'Video URL: {video_url}')


if __name__ == '__main__':
    main()
