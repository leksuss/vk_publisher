# Comics publisher to VK

This tool is for publish random [xkcd](https://xkcd.com/) comics with description to VK group.

## Requirements

 - python3
 - `environs`
 - `requests`

## How to install

Get the source code of this repo:
```
git clone https://github.com/leksuss/vk_publisher.git
```

Go to this script:
```
cd vk_publisher
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
# If you would like to install dependencies inside virtual environment, you should create it first.
pip3 install -r requirements.txt
```

## How to setup

To make this tool working you need `access_token` and `group_id` setted in `.env` file. Yoo can use `.env_example` as a template. 

#### Receiving group_id

`group_id` you can find in any photo url pusblished in your group. For example, in this url `group_id` is `123456789`:
```
https://vk.com/mycoolgroup?z=photo-123456789_987654321%2Falbum-123456789_00
```

#### Receiving access_token

    1. [Login to VK](https://vk.com/login) if not logged yet.
    2. [Create VK app](https://vk.com/editapp?act=create), select `standalone app`. Find app ID in settings, it looks like 8-digit number.
    3. Based on [this instruction](https://dev.vk.com/api/access-token/implicit-flow-user) generate auth url and follow by it. `client_id` is an app ID from step 2. Here is example of this url:
    ```
    https://oauth.vk.com/authorize?client_id=<YOUR_CLIENT_ID>&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&scope=offline,photos,manage,wall&v=5.131
    ```
    4. Copy `access_token` from params in redirected url and past it to `.env` file.


## How to use

Run script without arguments:
```
python3 main.py
```
One run - one published comics with description.
