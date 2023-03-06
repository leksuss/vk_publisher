import os
import pathlib
import random
from urllib.parse import urlparse

import requests


def fetch_last_published_id():

    url = 'https://xkcd.com/info.0.json'

    response = requests.get(url)
    response.raise_for_status()

    return response.json()['num']


def fetch_img_metadata(img_id):

    url = f'https://xkcd.com/{img_id}/info.0.json'

    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def fetch_and_save_img(url, filepath):

    response = requests.get(url)
    response.raise_for_status()

    with open(filepath, 'wb') as file:
        file.write(response.content)


def download_img(dirpath):

    last_img_id = fetch_last_published_id()

    random_img_id = random.randint(0, last_img_id + 1)
    img_metadata = fetch_img_metadata(random_img_id)

    img_url = img_metadata['img']
    img_text = img_metadata['alt']

    img_name = pathlib.Path(urlparse(img_url).path).name

    img_filepath = os.path.join(dirpath, img_name)
    fetch_and_save_img(img_url, img_filepath)

    return img_text, img_filepath
