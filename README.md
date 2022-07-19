# Get-photo-NASA-SAPCEX

## Description
This programm download photos from NASA and SPACEX resurses and post one photos once a day in Telegramm chanel.

## Install
Download and unpack ZIP file.

## Requirements
python 3
python-dotenv==0.19.2
environ==1.0
datetime==4.4
requests==2.26.0
python-telegram-bot==13.13

For download photos from NASA and SPACEX resurses require:
API token SPACE-X
API token NASA

For post photos in Telegramm chanel require:
Telegramm chat_id and Telegram bot token.

How does .env look like:
'''
NASA_API_TOKEN=######
TELEGRAM_API=######
CHAT_ID=######
EPIC_API_KEY=######
TIME_PERIOD=8400
'''

`TIME_PERIOD` is periodicity parameter of posting images in seconds.



## How to start
Open Windows command line and move to directory \Get photo NASA SAPCEX
To start programm you shuold use: `python main.py`
example:
```\Get photo NASA SAPCEX>python main.py
Posting a picture on telegram chanel: epic_1b_20220420072959.png
Next picture will be posted in 86400 seconds
```
