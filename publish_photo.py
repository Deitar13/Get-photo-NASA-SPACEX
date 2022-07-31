import os
import telegram
import random
import time

from dotenv import load_dotenv


def publish_photo_in_tg():
    time_period = int(os.environ['TIME_PERIOD'])
    tg_api_token = os.environ['TG_API_TOKEN']
    tg_channel_chat_id = os.environ['TG_CHAT_ID']
    message = 'telegram.error.NetworkError(message)'

    while True:
        try:
            bot = telegram.Bot(token=tg_api_token)
            images = os.listdir('images')
            random_image = random.choice(images)

            print('Posting a picture on tg chanel:', random_image)
            with open(os.path.join('images', random_image), 'rb') as file:
                bot.send_document(chat_id=tg_channel_chat_id,
                                  document=file)
            print(f'Next picture will be posted in: {time_period} seconds')
            time.sleep(time_period)
        except telegram.error.NetworkError(message):
            print('telegram.error.NetworkError(message)')



if __name__ == '__main__':
    load_dotenv()
    publish_photo_in_tg()
