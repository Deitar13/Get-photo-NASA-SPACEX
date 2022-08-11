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
python -m pip install -r requirements.txt
```

For download photos from NASA and SPACEX site require:
API token SPACE-X
API token NASA

For post photos in Telegramm channel require:
Telegramm chat_id and Telegram bot token.

How does .env look like:
```
NASA_API_TOKEN=######
TG_API_TOKEN=######
TG_CHAT_ID=######
FOLDER_NAME='images'
```
Default time period of posting images is 14400 seconds.
If you neet to set periodicity parameter.
You can add to .env file:
`TIME_PERIOD=your_number_of_seconds` 


## How to start

Run scripts:
example:
```
python fetch_earth_photos.py
```
```
python fetch_apod_photos.py
```

Script fetch_spacex_photos.py can get photos from appointed start number.
To do it you should use optional argument `launch_id`
```
python fetch_spacex_photos.py --launch_id 5eb87d42ffd86e000604b384
```
If you run script without optional argument, script will get photo from last start.

To publish photo in TG:
```
python publish_photo.py
```
result:
```
\Get photo NASA SAPCEX>python publish_photo.py
Posting a picture on telegram chanel: epic_1b_20220725114948.png
Next picture will be posted in: 14400 seconds
```
