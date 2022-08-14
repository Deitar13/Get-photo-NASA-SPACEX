import requests
import os
import datetime

from dotenv import load_dotenv
from save_photos import save_photo
from pathlib import Path


def get_epic_earth_photos_urls(folder_name, nasa_api_token):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_api_token}
    response = requests.get(epic_url, params=payload)
    response.raise_for_status()

    for photo_info in response.json():
        name = photo_info['image']
        name = f'{name}.png'
        date = datetime.datetime.fromisoformat(photo_info['date'])
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date:%Y/%m/%d}/png/{name}'
        save_photo(folder_name, name, url, payload)


if __name__ == '__main__':
    load_dotenv()
    nasa_api_token = os.environ['NASA_API_TOKEN']
    folder_name = os.getenv('FOLDER_NAME', default='images')
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    get_epic_earth_photos_urls(folder_name, nasa_api_token)
