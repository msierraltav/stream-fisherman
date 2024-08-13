import requests
import time
import json
import os
from dotenv import load_dotenv
from datetime import datetime
import re
import subprocess
import platform

load_dotenv()

endpoint = 'https://api.twitch.tv/helix/streams'
CLIENT_ID = os.getenv('CLIENT_ID')
OAUTH = os.getenv('OAUTH')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
USER_LOGIN = os.getenv('USER_LOGIN_NAME')
global stream_origin_name

# FILE_PATH = 'D:\\VideoProyects\\VOD\\auto'
#FILE_PATH = 'D:\\videos'
FILE_PATH = './videos'


def sanitize_filename(filename):
    # Replace all invalid characters with "_"
    filename = filename.replace(' ', '_')
    invalid_chars = "\\/:*?\"<>|"
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    filename = re.sub("_+", "_", filename)

    return filename

def remove_bracketed_text(text):
    return re.sub(r'\[[^\]]*\]|\([^\)]*\)', '', text)


# Obtener el token de acceso usando las credenciales
def get_access_token(client_id, client_secret):
    token_url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'client_credentials'
    }
    response = requests.post(token_url, params=params)
    data = response.json()
    return data.get('access_token')

def check_stream_online():
    stream_is_online = False

    params = {
        'client_id': CLIENT_ID,
        'user_login': USER_LOGIN
    }
    headers = {
        'Client-Id': CLIENT_ID,
        'Authorization': AUTH
    }
    try:
        stream_is_online = False
        response = requests.get(endpoint, params=params, headers=headers)
        data = json.loads(response.text)
        print(data)
        if len(data['data']) == 0:
            return False
        else:
            global stream_origin_name
            stream_origin_name = data['data'][0]['title']
            stream_is_online = True
    except requests.exceptions.RequestException as e:
        print(e)
        stream_is_online = False
    return stream_is_online

AUTH = (f'Bearer {get_access_token(CLIENT_ID, CLIENT_SECRET)}')
print(f'auth token : {AUTH}')

while True:
    try:
        isOnline = check_stream_online()
        if(isOnline):
            try:
                # set name 
                current_time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
                stream_name = sanitize_filename(remove_bracketed_text(stream_origin_name))
                video_name = f'{USER_LOGIN}_{current_time}'
                video_path = os.path.join(FILE_PATH,video_name)
                commandWin = f'streamlink "--twitch-api-header=Authorization=OAuth {OAUTH}" -o {video_path}.mkv https://www.twitch.tv/{USER_LOGIN} best'
                command = f'streamlink --twitch-api-header=Authorization="OAuth {OAUTH}" -o {video_path}.mkv https://www.twitch.tv/{USER_LOGIN} best'

                system = platform.system()

                print(f'\n\r{datetime.now().strftime("%Y-%m-%d %H-%M-%S")} > {USER_LOGIN} is online : start recording\n')
                print(f'Filename : {video_name} \nCurrent command: {command}\n')

                if system == 'Windows':
                    process = subprocess.Popen(f"cmd /k {commandWin}", creationflags=subprocess.DETACHED_PROCESS | subprocess.CREATE_NEW_PROCESS_GROUP)
                    # os.system(f"cmd /k {command}")
                else:
                    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

                process.wait()
                print(f'{datetime.now().strftime("%Y-%m-%d %H-%M-%S")} > {USER_LOGIN} strean ended.\n')
            except Exception as e:
                print(e)

        else:
            print (f'{datetime.now().strftime("%Y-%m-%d %H-%M-%S")} > {USER_LOGIN} offline :c \r', end='', flush=True)
        
    except Exception as e:
        print(e)
        continue

    time.sleep(180)

