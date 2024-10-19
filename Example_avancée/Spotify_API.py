import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build

# Configuration des API
SPOTIPY_CLIENT_ID = 'YOUR_SPOTIFY_CLIENT_ID'
SPOTIPY_CLIENT_SECRET = 'YOUR_SPOTIFY_CLIENT_SECRET'
SPOTIPY_REDIRECT_URI = 'http://localhost:8888/callback'
YOUTUBE_API_KEY = 'YOUR_YOUTUBE_API_KEY'

# Authentification Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='playlist-modify-private'))

# Fonction pour obtenir les morceaux likés sur YouTube
def get_liked_songs_youtube():
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    
    request = youtube.videos().list(
        part='snippet',
        mySubscribers=True,
        maxResults=50,
        pageToken=None
    )
    response = request.execute()
    
    liked_songs = []
    
    for item in response.get('items', []):
        title = item['snippet']['title']
        liked_songs.append(title)
    
    return liked_songs

# Fonction pour créer une playlist Spotify
def create_spotify_playlist(playlist_name):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, playlist_name, public=False)
    return playlist['id']

# Fonction pour ajouter des morceaux à la playlist
def add_tracks_to_playlist(playlist_id, track_titles):
    for title in track_titles:
        results = sp.search(q=title, type='track', limit=1)
        if results['tracks']['items']:
            track_id = results['tracks']['items'][0]['id']
            sp.playlist_add_items(playlist_id, [track_id])

if __name__ == "__main__":
    # Obtenir les morceaux likés sur YouTube
    liked_songs = get_liked_songs_youtube()
    
    # Créer une nouvelle playlist sur Spotify
    playlist_name = input("Entrez le nom de votre playlist : ")
    playlist_id = create_spotify_playlist(playlist_name)
    
    # Ajouter les morceaux à la playlist
    add_tracks_to_playlist(playlist_id, liked_songs)
    
    print(f"La playlist '{playlist_name}' a été créée et les morceaux ajoutés.")
