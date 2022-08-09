import os
import requests

from dotenv import load_dotenv
from save_photos import save_photo
from get_extension import get_extension_url
from pathlib import Path


def get_apod_photos(folder_name, nasa_api_token):

    count_apod_photos = 5
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_token,
        'count': count_apod_photos
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    for urls_count, item in enumerate(response.json(), 1):
        extension = get_extension_url(item['url'])
        name = f'apod{urls_count}{extension}'
        if item['media_type'] == 'image':
            save_photo(folder_name, name, item['url'])


if __name__ == '__main__':
    load_dotenv()
    folder_name = 'images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    nasa_api_token = os.environ['NASA_API_TOKEN']
    get_apod_photos(folder_name, nasa_api_token)
