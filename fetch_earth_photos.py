import argparse
import requests
import os
import datetime


from dotenv import load_dotenv
from save_photos import save_photo
from pathlib import Path


def get_epic_earth_photos_urls(folder_name):
    nasa_api_token = os.environ['NASA_API_TOKEN']
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': nasa_api_token}
    response = requests.get(epic_url, params=payload)
    response.raise_for_status()

    for photo_info in response.json():
        name = photo_info['image']
        name = f'{name}.png'
        date_of_photo = datetime.datetime.fromisoformat(photo_info['date'])
        date = date_of_photo.strftime('%Y/%m/%d')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}'
        payload = {'api_key': f'{nasa_api_token}'}
        response = requests.get(url, params=payload)
        response.raise_for_status()
        content = response.content
        save_photo(folder_name, name, content)


if __name__ == '__main__':
    load_dotenv()
    folder_name = 'images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    get_epic_earth_photos_urls(folder_name)
