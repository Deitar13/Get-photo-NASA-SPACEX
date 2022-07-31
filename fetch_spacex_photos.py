import argparse
import requests

from dotenv import load_dotenv
from save_photos import save_photo
from pathlib import Path


def fetch_spacex_last_launch(folder_name, launch_number=False):
    url = 'https://api.spacexdata.com/v3/launches/'
    links = []
    response = requests.get(url)
    response.raise_for_status()

    if launch_number:
        for item in response.json():
            if item['flight_number'] == int(launch_number):
                if item['links']['flickr_images']:
                    photos_links = item['links']['flickr_images']
                else:
                    print(f'flight_number {launch_number} have no any photos')
                    print('try another "flight_number"')
                    return

    else:
        for item in response.json():
            if item['links']['flickr_images']:
                links.append(item['links']['flickr_images'])
        photos_links = links[-1]

    for photo_number, link in enumerate(photos_links, 1):
        name = f'spacex{photo_number}.jpg'
        response = requests.get(link)
        response.raise_for_status()
        content = response.content
        save_photo(folder_name, name, content)


if __name__ == '__main__':
    load_dotenv()
    folder_name = 'images'
    Path(folder_name).mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser()
    parser.add_argument('--launch_number')
    args = parser.parse_args()
    if args.launch_number:
        launch_number = args.launch_number
        fetch_spacex_last_launch(folder_name, launch_number=args.launch_number)
    else:
        fetch_spacex_last_launch(folder_name)
