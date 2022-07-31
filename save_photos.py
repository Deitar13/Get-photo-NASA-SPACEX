import os
import os.path


def save_photo(folder_name, name, content):
    with open(os.path.join(folder_name, name), 'wb') as file:
        file.write(content)

