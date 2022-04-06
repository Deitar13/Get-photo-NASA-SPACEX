import datetime
import os
import os.path
import random
import time

import requests
import telegram

from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlsplit, urlparse


def ensure_dir(file_path):
    Path(file_path).mkdir(parents=True, exist_ok=True)


def get_extension(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    return os.path.splitext(path)[1]


def fetch_apod_photos(file_path, nasa_api_token, count_apod_photos):
    nasa_url = "https://api.nasa.gov/planetary/apod"
    payload = {"api_key": f"{nasa_api_token}", "count": f"{count_apod_photos}"}
    response = requests.get(nasa_url, params=payload)
    response.raise_for_status()
    urls_count = 0

    for item in response.json():
        parsed_url = urlparse(item['url'])

        urls_count += 1
        extension = get_extension(item['url'])
        photo_name = (f"apod{urls_count}{extension}")
        response = requests.get(item['url'])
        response.raise_for_status
        with open(f"{file_path}/{photo_name}", 'wb') as file:
            file.write(response.content)


def fetch_spacex_last_launch(file_path):
    url = 'https://api.spacexdata.com/v3/launches/'
    links_list = []
    response = requests.get(url)
    response.raise_for_status

    for item in response.json():
        if item["links"]["flickr_images"]:
            links_list.append(item["links"]["flickr_images"])
    last_photos_links = links_list[-1]

    for photo_number, link in enumerate(last_photos_links, 1):
        image_name = (f"spacex{photo_number}.jpg")
        response = requests.get(link)
        response.raise_for_status
        with open(f"{file_path}/{image_name}", 'wb') as file:
            file.write(response.content)


def get_epic_earth_photos_urls(file_path):
    epic_url = 'https://api.nasa.gov/EPIC/api/natural/images?api_key=DEMO_KEY'
    response = requests.get(epic_url)
    response.raise_for_status()

    for photo_info in response.json():
        name_of_photo = photo_info["image"]
        date_of_photo = datetime.datetime.fromisoformat(photo_info["date"])
        formatted_date_of_photo = date_of_photo.strftime("%Y/%m/%d")
        epic_earth_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{formatted_date_of_photo}/png/{name_of_photo}.png?api_key=DEMO_KEY'
        download_epic_earth_photo(epic_earth_photo_url, name_of_photo)


def download_epic_earth_photo(epic_earth_photo_url, name_of_photo):
    response = requests.get(epic_earth_photo_url)
    response.raise_for_status
    with open(f"{file_path}/{name_of_photo}.png", 'wb') as file:
        file.write(response.content)

if __name__ == "__main__":
    load_dotenv()
    nasa_api_token = os.environ["NASA_API_TOKEN"]
    telegram_api_token = os.environ["TELEGRAM_API"]
    telegram_channel_chat_id = os.environ["CHAT_ID"]
    file_path = "images"

    ensure_dir(file_path)
    fetch_spacex_last_launch(file_path)
    count_apod_photos = 5
    fetch_apod_photos(file_path, nasa_api_token, count_apod_photos)
    get_epic_earth_photos_urls(file_path)

    while True:

        time_period = 86400
        bot = telegram.Bot(token=f'{telegram_api_token}')
        print(bot.get_me())
        images = os.listdir('images')
        random_image = random.choice(images)

        print("опубликовать данную картинку:", random_image)
        bot.send_document(chat_id=telegram_channel_chat_id, document=open(f'images/{random_image}', 'rb'))
        time.sleep(time_period)
