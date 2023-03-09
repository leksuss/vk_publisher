import requests


VK_API_VERSION = 5.131


def fetch_vk_upload_server_url(group_id, api_key):

    url = 'https://api.vk.com/method/photos.getWallUploadServer'

    params = {
        'group_id': group_id,
        'access_token': api_key,
        'v': VK_API_VERSION,
    }
    response = requests.post(url, data=params)
    response.raise_for_status()

    return response.json()['response']['upload_url']


def upload_img_to_vk_server(upload_url, filepath):

    with open(filepath, 'rb') as file:
        files = {
            'photo': file,
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()

    return response.json()


def save_img_to_vk_server(group_id, photo, server, hash, api_key):

    url = 'https://api.vk.com/method/photos.saveWallPhoto'

    params = {
        'group_id': group_id,
        'photo': photo,
        'server': server,
        'hash': hash,
        'access_token': api_key,
        'v': VK_API_VERSION,
    }
    response = requests.post(url, data=params)
    response.raise_for_status()

    return response.json()['response']


def post_img_to_vk_wall(group_id, owner_id, media_id, message, api_key):

    url = 'https://api.vk.com/method/wall.post'

    params = {
        'owner_id': f'-{group_id}',
        'message': message,
        'attachments': f'photo1653853_{media_id}',
        'from_group': 1,
        'access_token': api_key,
        'v': VK_API_VERSION,
    }
    response = requests.post(url, data=params)
    response.raise_for_status()

    return response.json()


def publish_post(group_id, img_text, img_filepath, api_key):

    vk_upload_server_url = fetch_vk_upload_server_url(group_id, api_key)

    upload_response = upload_img_to_vk_server(
        vk_upload_server_url,
        img_filepath,
    )

    saved_pic = save_img_to_vk_server(
        group_id,
        upload_response['photo'],
        upload_response['server'],
        upload_response['hash'],
        api_key
    )

    publish_status = post_img_to_vk_wall(
        group_id,
        saved_pic[0]['owner_id'],
        saved_pic[0]['id'],
        img_text,
        api_key,
    )

    return publish_status['response']
