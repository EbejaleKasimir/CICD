import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy import SpotifyClientCredentials

client_id = '1766a7df93394253ac2fa004272ab59d'
client_secret = '2b9f578d4da94bc9afcf5353bdde84ea'
redirect_uri = 'http://localhost:8081/callback'  # replace with your redirect_uri
scope = 'playlist-read-private'  # replace with your needed scopes

auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist_url = 'https://open.spotify.com/playlist/2khn1j2muqFCP1bZveUgEt'

playlist_id = playlist_url.split('/')[-1]

data = sp.playlist_tracks(playlist_id)

# Print the data
for i, item in enumerate(data['items']):
    track = item['track']
    print(f"{i} {track['artists'][0]['name']} – {track['name']}")
