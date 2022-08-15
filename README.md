# Get-photo-NASA-SPACEX

## Description
This program download photos from NASA and SPACEX site and post one photos once a day in Telegram channel.

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

For post photos in Telegram channel require:
Telegram chat_id and Telegram bot token.

How does .env look like:
```
NASA_API_TOKEN=######
TG_API_TOKEN=######
TG_CHAT_ID=######
```
Default time period of posting images is 14400 seconds.
If you neet to set periodicity parameter.
You can add to .env file:
`TIME_PERIOD=your_number_of_seconds` 

Default numbers of apod photos for downloading is 5, to set numbers you can add to .env file:
`COUNT_APOD_PHOTOS=your_number`

Default name of folder to downloading all photos is 'images', to set folder you can add to .env file:
`FOLDER_NAME='your_folder'`


## How to start

Run scripts:
example:
```
python fetch_earth_photos.py
```
```
python fetch_apod_photos.py
```
Also you can set numbers of photos by the optional argument `count_photos`, default is 5.

```
python fetch_apod_photos.py --count_photos 2
```

Script fetch_spacex_photos.py can get photos from appointed rocket start number.
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
