import os
import requests
#import get_extension

from dotenv import load_dotenv
from safePhoto import safe_photo
from get_extension import get_extension_url
from pathlib import Path


def get_apod_photos(file_path):
    nasa_api_token = os.environ['NASA_API_TOKEN']
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
        response = requests.get(item['url'])
        response.raise_for_status()
        safe_photo(file_path, name, response)


if __name__ == '__main__':
    load_dotenv()
    file_path = 'images'
    Path(file_path).mkdir(parents=True, exist_ok=True)
    get_apod_photos(file_path)
