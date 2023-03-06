import os
import pathlib

from environs import Env

import downloader
import publisher


DOWNLOAD_FOLDER = 'files'


def main():

    env = Env()
    env.read_env()

    group_id = env.str('VK_GROUP_ID')
    api_key = env.str('VK_API_KEY')

    pathlib.Path(DOWNLOAD_FOLDER).mkdir(exist_ok=True)

    img_text, img_filepath = downloader.download_img(DOWNLOAD_FOLDER)

    publish_status = publisher.publish_post(
        group_id,
        img_text,
        img_filepath,
        api_key,
    )

    if publish_status['post_id']:
        os.remove(img_filepath)
        post_url = 'https://vk.com/club{}?w=wall-{}_{}'.format(
            group_id,
            group_id,
            publish_status['post_id'],
        )
        msg = f'Your post is published, here is the link:\n{post_url}'
    else:
        msg = "Unfortunately, your post wasn't published :("

    print(msg)


if __name__ == '__main__':
    main()
