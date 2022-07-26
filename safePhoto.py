import os
import os.path


def safe_photo(file_path, name, response):
    with open(os.path.join(file_path, name), 'wb') as file:
        file.write(response.content)
        print(os.path.join(file_path, name))
