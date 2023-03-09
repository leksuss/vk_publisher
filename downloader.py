import random

import requests


def fetch_last_published_img_id():

    url = 'https://xkcd.com/info.0.json'

    response = requests.get(url)
    response.raise_for_status()

    return response.json()['num']


def fetch_img_metadata(img_id):

    url = f'https://xkcd.com/{img_id}/info.0.json'

    response = requests.get(url)
    response.raise_for_status()

    return response.json()


def download_random_img(img_filepath):

    last_img_id = fetch_last_published_img_id()

    random_img_id = random.randint(0, last_img_id + 1)
    img_metadata = fetch_img_metadata(random_img_id)

    img_url = img_metadata['img']
    img_text = img_metadata['alt']

    response = requests.get(img_url)
    response.raise_for_status()

    with open(img_filepath, 'wb') as file:
        file.write(response.content)

    return img_text
