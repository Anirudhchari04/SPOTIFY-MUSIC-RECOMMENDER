from flask import Flask, render_template, request, redirect, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# Spotify API setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='a3e2bc14bc4a47028377a35c85a4559c',
                                               client_secret='f83a966ead284c1bbed3228405e7243b',
                                               redirect_uri='https://open.spotify.com/',
                                               scope='playlist-modify-public'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        artist_name = request.form['artist_name']
        song_name = request.form['song_name']

        # Your recommendation logic here
        song_info = get_song_info(artist_name, song_name)
        if song_info:
            seed_track_id = song_info['id']
            recommended_tracks = get_recommendations(seed_track_id)

            # Create a new playlist and add recommended tracks
            playlist_name = f"Recommended Songs for {song_name} by {artist_name}"
            playlist_description = "A playlist of recommended songs based on the selected track."
            playlist_id = create_playlist(playlist_name, playlist_description)
            track_ids = [track['id'] for track in recommended_tracks]
            add_tracks_to_playlist(playlist_id, track_ids)

    return render_template('index.html')

def get_song_info(artist_name, song_name):
    results = sp.search(q=f"artist:{artist_name} track:{song_name}", type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        return track
    else:
        print("Song not found.")
        return None

artist_name = "Artist Name"
song_name = "Song Name"
song_info = get_song_info(artist_name, song_name)


def get_recommendations(seed_track_id):
    recommendations = sp.recommendations(seed_tracks=[seed_track_id], limit=10)
    return recommendations['tracks']

if song_info:
    seed_track_id = song_info['id']
    recommended_tracks = get_recommendations(seed_track_id)


def create_playlist(name, description):
    user_info = sp.current_user()
    user_id = user_info['id']
    playlist = sp.user_playlist_create(user_id, name, public=True, description=description)
    return playlist['id']

def add_tracks_to_playlist(playlist_id, track_ids):
    sp.playlist_add_items(playlist_id, track_ids)

# Create a new playlist and add recommended tracks
playlist_name = "Recommended Songs Playlist"
playlist_description = "A playlist of recommended songs based on the selected track."
playlist_id = create_playlist(playlist_name, playlist_description)
track_ids = [track['id'] for track in recommended_tracks]
add_tracks_to_playlist(playlist_id, track_ids)


if __name__ == '__main__':
    app.run(debug=True)
