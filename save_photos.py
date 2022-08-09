import os
import os.path
import requests


def save_photo(folder_name, name, url, payload=None):
    response = requests.get(url, params=payload)
    response.raise_for_status()
    content = response.content
    with open(os.path.join(folder_name, name), 'wb') as file:
        file.write(content)
        print(folder_name, name, 'saved')
