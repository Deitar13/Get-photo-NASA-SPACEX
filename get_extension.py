import os.path
from urllib.parse import urlparse


def get_extension_url(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    return os.path.splitext(path)[1]
