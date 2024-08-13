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
def get_vtuber_users(access_token, cursor=None):
    headers = {
        'Client-ID': client_id,
        'Authorization': f'Bearer {access_token}'
    }
    search_url = 'https://api.twitch.tv/helix/search/channels'
    params = {
        'query': 'vtuber',
        'first': 100  # Número de resultados por página
    }
    if cursor:
        params['after'] = cursor
    response = requests.get(search_url, headers=headers, params=params)
    data = response.json()
    return data

access_token = get_access_token(client_id, client_secret)

all_filtered_users = []

cursor = None
while True:
    response_data = get_vtuber_users(access_token, cursor)
    vtuber_users = response_data.get('data', [])
    all_filtered_users.extend([user for user in vtuber_users if 'Español' in user['tags']])
    
    cursor = response_data.get('pagination', {}).get('cursor')
    if not cursor:
        break

# Imprimir los usuarios filtrados en la consola
for user in all_filtered_users:
    username = user['broadcaster_login']
    profile_name = user['display_name']
    profile_picture = user['thumbnail_url']
    print(f"Username: {username} (Profile Name: {profile_name}), Profile Picture: {profile_picture}")
