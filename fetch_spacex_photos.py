import argparse
import requests

from dotenv import load_dotenv
from save_photos import save_photo
from pathlib import Path


def get_photos_links(url):
    response = requests.get(url)
    response.raise_for_status()
    launch = response.json()

    if not launch['links']['flickr']['original']:
        launch_date = launch['date_local']
        print(f'{launch_date} launch have no any photos')

    else:
        photos_links = launch['links']['flickr']['original']
        return photos_links


def transfer_to_save(photos_links):

    for photo_number, link in enumerate(photos_links, 1):
        name = f'spacex{photo_number}.jpg'
        save_photo(folder_name, name, link)


def fetch_spacex_last_launch(folder_name, launch_id=False):

    if launch_id:
        url = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        photos_links = get_photos_links(url)
        transfer_to_save(photos_links)

    else:
        url = 'https://api.spacexdata.com/v5/launches/latest'
        photos_links = get_photos_links(url)
        if photos_links:
            transfer_to_save(photos_links)


if __name__ == '__main__':
    load_dotenv()
    folder_name = 'images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_id')
    args = parser.parse_args()

    if args.launch_id:
        launch_number = args.launch_id
        fetch_spacex_last_launch(folder_name, launch_id=args.launch_id)

    else:
        fetch_spacex_last_launch(folder_name)
