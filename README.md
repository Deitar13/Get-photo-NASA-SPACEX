# Get-photo-NASA-SPACEX

## Description
This program download photos from NASA and SPACEX site and post one photos once a day in Telegramm channel.

## Install
Download and unpack ZIP file.

## Requirements

python 3
pip

packages:
```
pip install python-dotenv==0.19.2
pip install environ==1.0
pip install datetime==4.4
pip install requests==2.26.0
pip install python-telegram-bot==13.13
```

For download photos from NASA and SPACEX site require:
API token SPACE-X
API token NASA

For post photos in Telegramm channel require:
Telegramm chat_id and Telegram bot token.

How does .env look like:
```
NASA_API_TOKEN=######
TELEGRAM_API=######
TG_CHAT_ID=######
EPIC_API_KEY=######
TIME_PERIOD=8400
```

`TIME_PERIOD` is periodicity parameter of posting images in seconds.


## How to start

Run scripts:
example:
```
\Get photo NASA SAPCEX>python fetch_earth_photos.py
images\epic_1b_20220727001752.png
images\epic_1b_20220727012319.png
images\epic_1b_20220727022846.png
images\epic_1b_20220727033413.png
```

```
>python fetch_apod_photos.py
images\apod1.jpg
images\apod2.jpg
images\apod3.gif
images\apod4.jpg
images\apod5.jpg
```

```
\Get photo NASA SAPCEX>python main.py
To get SpaceX last launch photo input: 1
To get epic Earth photos input: 2
To get NASA APOD photos input: 3
To post random picture on TG channel input: 4
3
images/apod1.jpg
images/apod2.jpg
images/apod3.jpg
images/apod4.jpg
images/apod5.jpg
```
Script fetch_spacex_photos.py can get photos from appointed start number.
To do it you should use optional argument `launch_number`

```Get photo NASA SAPCEX>python fetch_spacex_photos.py --launch_number 94
images\spacex1.jpg
images\spacex2.jpg
images\spacex3.jpg
images\spacex4.jpg
images\spacex5.jpg
```
If you run script without optional argument, script will get photo from last start.


```
\Get photo NASA SAPCEX>python publish_photo.py
Posting a picture on telegram chanel: epic_1b_20220725114948.png
Next picture will be posted in: 8400 seconds
```
