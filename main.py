import argparse
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
from get_extension import get_extension_url
import fetch_spacex_images
import publish_photo
from publish_photo import publish_photo_in_tg
import fetch_apod_photos
from fetch_apod_photos import get_apod_photos
import fetch_epic_earth_photos_urls
from fetch_epic_earth_photos_urls import get_epic_earth_photos_urls


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
#        parser = argpars.ArgumentParser()
#        parser.parser_args()
        fetch_spacex_images.fetch_spacex_last_launch(file_path)

    if user_choice == 2:
        fetch_epic_earth_photos_urls.get_epic_earth_photos_urls(file_path)
    if user_choice == 3:
        fetch_apod_photos.get_apod_photos(file_path)
    if user_choice == 4:
        publish_photo.publish_photo_in_tg()
