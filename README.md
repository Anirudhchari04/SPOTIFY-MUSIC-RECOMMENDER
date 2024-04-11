# SPOTIFY-MUSIC-RECOMMENDER
This Flask application utilizes the Spotify API to generate recommended songs based on a user-selected track and creates a new public playlist on the user's Spotify account containing the recommendations.
**README**

**Description:**
This Flask application utilizes the Spotify API to create a web-based tool for generating recommended songs based on a user-selected track. Upon entering an artist's name and a song title, the application searches for the track on Spotify and retrieves its information. Using this information, it then fetches recommendations from Spotify's recommendation engine based on the selected track. The recommended tracks are added to a new public playlist on the user's Spotify account, which is created by the application. 

**Dependencies:**
- Flask
- Spotipy

**Setup:**
1. Install the required dependencies using `pip install flask spotipy`.
2. Replace the `client_id` and `client_secret` in the `SpotifyOAuth` constructor with your own Spotify API credentials.
3. Ensure that the `redirect_uri` matches the one specified in your Spotify API application settings.
4. Run the Flask application using `python app.py`.
5. Access the application in your web browser at `http://localhost:5000`.

**Usage:**
1. Enter the artist's name and the song title in the input fields provided on the home page.
2. Click on the submit button to generate recommended songs based on the selected track.
3. A new public playlist will be created on your Spotify account, containing the recommended songs.

**Notes:**
- Ensure that you have a Spotify account and are logged in to use this application.
- The application fetches recommendations based on the track's popularity, genre, and other factors analyzed by Spotify's recommendation engine.

**Disclaimer:**
This application is for educational and demonstration purposes only. Use it responsibly and respect Spotify's terms of service and API usage policies.
