import requests
import spotipy
from spotipy import SpotifyClientCredentials

def get_user_playlists(username):
    client = spotipy.Spotify(auth=requests.auth.HTTPBasicAuth(username, "YOUR_PASSWORD"))
    playlists = client.user_playlists(username)
    return playlists

if __name__ == "__main__":
    playlists = get_user_playlists("YOUR_USERNAME")
    print(playlists)


client_id = '1766a7df93394253ac2fa004272ab59d'
client_secret = '2b9f578d4da94bc9afcf5353bdde84ea'

client_credentials_manager=SpotifyClientCredentials(client_id=client_id,client_secret=client_secret)

sp=spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_url = 'https://open.spotify.com/playlist/2khn1j2muqFCP1bZveUgEt'

playlist_url_new = playlist_url.split('/')[-1]

playlist_url_new

sp.playlist_tracks(playlist_url_new)

data = sp.playlist_tracks(playlist_url_new)

data