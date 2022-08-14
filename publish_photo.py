import os
import telegram
import random
import time

from dotenv import load_dotenv


def publish_photo_in_tg(tg_api_token, tg_channel_chat_id, time_period):

    while True:
        try:
            bot = telegram.Bot(token=tg_api_token)
            folder_name = os.getenv('FOLDER_NAME', default='images')
            images = os.listdir(folder_name)
            random_image = random.choice(images)
            print('Posting a picture on tg chanel:', random_image)
            with open(os.path.join(folder_name, random_image), 'rb') as file:
                bot.send_document(chat_id=tg_channel_chat_id,
                                  document=file)
            print(f'Next picture will be posted in: {time_period} seconds')
            time.sleep(time_period)
        except telegram.error.NetworkError:
            print('telegram.error.NetworkError will try again in 1 second')
            time.sleep(1)


if __name__ == '__main__':
    load_dotenv()
    tg_api_token = os.environ['TG_API_TOKEN']
    tg_channel_chat_id = os.environ['TG_CHAT_ID']
    time_period = os.getenv('TIME_PERIOD', default=14400)
    publish_photo_in_tg(tg_api_token, tg_channel_chat_id, time_period)
