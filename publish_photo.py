import os
import telegram
import random
import time


def publish_photo_in_tg():
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
