import os
import requests

from dotenv import load_dotenv
from save_photos import save_photo
from pathlib import Path
from urllib.parse import urlparse


def get_extension_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    return os.path.splitext(path)[1]


def get_apod_photos(folder_name, nasa_api_token):

    count_apod_photos = os.getenv('COUNT_APOD_PHOTOS', default=5)
    nasa_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        'api_key': nasa_api_token,
        'count': count_apod_photos
    }
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    for urls_count, item in enumerate(response.json(), start=1):
        extension = get_extension_url(item['url'])
        name = f'apod{urls_count}{extension}'
        if item['media_type'] == 'image':
            save_photo(folder_name, name, item['url'])


if __name__ == '__main__':
    load_dotenv()
    folder_name = os.getenv('FOLDER_NAME', default='images')
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    nasa_api_token = os.environ['NASA_API_TOKEN']
    get_apod_photos(folder_name, nasa_api_token)
