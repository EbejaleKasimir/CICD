import os
import requests
import base64
import pprint

# Get your Spotify Client ID and Secret from environment variables
client_id = os.getenv('SPOTIFY_CLIENT_ID')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')

# Encode the credentials in base64
credentials = base64.b64encode(f'{client_id}:{client_secret}'.encode('utf-8')).decode('utf-8')

# Get an access token
response = requests.post(
    'https://accounts.spotify.com/api/token',
    headers={'Authorization': f'Basic {credentials}'},
    data={'grant_type': 'client_credentials'}
)
response.raise_for_status()
access_token = response.json()['access_token']

# Use the access token to make requests to the Spotify API
headers = {'Authorization': f'Bearer {access_token}'}
response = requests.get('https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V', headers=headers)
response.raise_for_status()
track_data = response.json()

# Pretty-print the track data
pprint.pprint(track_data)

# Or, print specific pieces of information
print(f"Track name: {track_data['name']}")
print(f"Artist: {track_data['artists'][0]['name']}")
print(f"Album: {track_data['album']['name']}")
