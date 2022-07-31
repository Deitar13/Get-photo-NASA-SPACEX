import os
import os.path


def save_photo(folder_name, name, response):
    with open(os.path.join(folder_name, name), 'wb') as file:
        file.write(response.content)
        print(response.content)
