import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Credenciales de la API de Twitch
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

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

# Obtener usuarios con la etiqueta "vtuber"
def get_vtuber_users(access_token):
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    search_url = 'https://api.twitch.tv/helix/search/channels'
    params = {
        'query': 'vtuber'
    }
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()
    return data.get('data', [])

access_token = get_access_token(client_id, client_secret)
vtuber_users = get_vtuber_users(access_token)

for user in vtuber_users:
    username = user['broadcaster_login']
    profile_name = user['display_name']
    tags = user['tags']
    profile_picture = user['thumbnail_url']
    # follower_count = user['follower_count']
    print(f"Username: {username} (profile_name), Profile Picture: {profile_picture}, Tags: {tags}\n")
