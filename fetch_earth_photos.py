import argparse
import requests
import os
import datetime
#import safePhoto


from dotenv import load_dotenv
from safePhoto import safe_photo
from pathlib import Path


def get_epic_earth_photos_urls(file_path):
    epic_api_key = os.environ['EPIC_API_KEY']
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images'
    payload = {'api_key': epic_api_key}
    response = requests.get(epic_url, params=payload)
    response.raise_for_status()

    for photo_info in response.json():
        name = photo_info['image']
        name = f'{name}.png'
        date_of_photo = datetime.datetime.fromisoformat(photo_info['date'])
        date = date_of_photo.strftime('%Y/%m/%d')
        url = f'https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}'
        payload = {'api_key': f'{epic_api_key}'}
        response = requests.get(url, params=payload)
        response.raise_for_status()
        safe_photo(file_path, name, response)


if __name__ == '__main__':
#    parser = argparse.ArgumentParser()
#    parser.add_argument("file_path")
#    file_path = parser.parse_args()
#    print(file_path)
    load_dotenv()
    file_path = 'images'
    Path(file_path).mkdir(parents=True, exist_ok=True)
    get_epic_earth_photos_urls(file_path)

#python fetch_earth_photos.py images