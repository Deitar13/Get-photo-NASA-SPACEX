import requests

def fetch_spacex_last_launch(file_path):
    url = 'https://api.spacexdata.com/v3/launches/'
    links_list = []
    response = requests.get(url)
    response.raise_for_status()

    for item in response.json():
        if item['links']['flickr_images']:
            links_list.append(item['links']['flickr_images'])
    last_photos_links = links_list[-1]

    for photo_number, link in enumerate(last_photos_links, 1):
        name = f'spacex{photo_number}.jpg'
        response = requests.get(link)
        response.raise_for_status()
        safe_photo(name, response)
