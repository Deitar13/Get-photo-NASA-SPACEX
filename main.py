import datetime
import os
import os.path
import random
import time

import requests
import telegram

from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse


def get_extension(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    return os.path.splitext(path)[1]


def fetch_apod_photos(file_path):
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

        extension = get_extension(item['url'])
        name = f'apod{urls_count}{extension}'
        response = requests.get(item['url'])
        response.raise_for_status()
        safe_photo(name, response)


def fetch_spacex_last_launch(file_path):
    url = 'https://api.spacexdata.com/v3/launches/'
    links_list = []
    response = requests.get(url)
    response.raise_for_status()

    for item in response.json():
        if item['links']['flickr_images']:
            links_list.append(item['links']['flickr_images'])
    last_photos_links = links_list[-1]

    for photo_number, link in enumerate(last_photos_links, 1):
        name = f'spacex{photo_number}.jpg'
        response = requests.get(link)
        response.raise_for_status()
        safe_photo(name, response)


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
        safe_photo(name, response)


def safe_photo(name, response):
    with open(os.path.join(file_path, name), 'wb') as file:
        file.write(response.content)
        print(os.path.join(file_path, name))


def publish_photo():
    time_period = int(os.environ['TIME_PERIOD'])
    telegram_api_token = os.environ['TELEGRAM_API']
    telegram_channel_chat_id = os.environ['TG_CHAT_ID']

    while True:
        bot = telegram.Bot(token=f'{telegram_api_token}')
        images = os.listdir('images')
        random_image = random.choice(images)

        print('Posting a picture on telegram chanel:', random_image)
        with open(os.path.join('images', random_image), 'rb') as file_for_send:
            bot.send_document(chat_id=telegram_channel_chat_id,
                              document=file_for_send)
        print(f'Next picture will be posted in: {time_period} seconds')
        time.sleep(time_period)


if __name__ == '__main__':
    load_dotenv()
    file_path = 'images'
    Path(file_path).mkdir(parents=True, exist_ok=True)

    print("To get SpaceX last launch photo input: 1")
    print("To get epic Earth photos input: 2")
    print("To get NASA APOD photos input: 3")
    print("To post random picture on TG channel input: 4")
    user_choice = int(input())
    if user_choice == 1:
        fetch_spacex_last_launch(file_path)
    if user_choice == 2:
        get_epic_earth_photos_urls(file_path)
    if user_choice == 3:
        fetch_apod_photos(file_path)
    if user_choice == 4:
        publish_photo()
