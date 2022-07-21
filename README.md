# Get-photo-NASA-SAPCEX

## Description
This programm download photos from NASA and SPACEX resurses and post one photos once a day in Telegramm chanel.

## Install
Download and unpack ZIP file.

## Requirements

python 3
pip

packages:
'''
pip install python-dotenv==0.19.2
pip install environ==1.0
pip install datetime==4.4
pip install requests==2.26.0
pip install python-telegram-bot==13.13
'''

For download photos from NASA and SPACEX resurses require:
API token SPACE-X
API token NASA

For post photos in Telegramm chanel require:
Telegramm chat_id and Telegram bot token.

How does .env look like:
'''
NASA_API_TOKEN=######
TELEGRAM_API=######
TG_CHAT_ID=######
EPIC_API_KEY=######
TIME_PERIOD=8400
'''

`TIME_PERIOD` is periodicity parameter of posting images in seconds.



## How to start
Open Windows command line and move to directory \Get photo NASA SAPCEX
To start programm you shuold use: `python main.py`
example:
```\Get photo NASA SAPCEX>python main.py```
Script examples:
```
\Get photo NASA SAPCEX>python main.py
To get SpaceX last launch photo input: 1
To get epic Earth photos input: 2
To get NASA APOD photos input: 3
To post random picture on TG channel input: 4
1
images/spacex1.jpg
images/spacex2.jpg
images/spacex3.jpg
images/spacex4.jpg
images/spacex5.jpg
images/spacex6.jpg
```
```
\Get photo NASA SAPCEX>python main.py
To get SpaceX last launch photo input: 1
To get epic Earth photos input: 2
To get NASA APOD photos input: 3
To post random picture on TG channel input: 4
2
images/epic_1b_20220720043941.png
images/epic_1b_20220720054508.png
images/epic_1b_20220720065035.png
images/epic_1b_20220720075602.png
images/epic_1b_20220720090130.png
images/epic_1b_20220720100657.png
images/epic_1b_20220720111224.png
images/epic_1b_20220720121751.png
images/epic_1b_20220720132319.png
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

```
\Get photo NASA SAPCEX>python main.py
To get SpaceX last launch photo input: 1
To get epic Earth photos input: 2
To get NASA APOD photos input: 3
To post random picture on TG channel input: 4
4
Posting a picture on telegram chanel: apod1.jpg
Next picture will be posted in: 8400 seconds
```