import os
import spotipy
import dotenv
dotenv.load_dotenv()


class SpotifyClientManager:
    def __init__(self) -> None:
        self.scope = 'playlist-modify-private'
        self.user_id = os.getenv('SPOTIFY_USER_ID')
        self.client_id = os.getenv('SPOTIFY_CLIENT_ID')
        self.client_secret = os.getenv('SPOTIFY_CLIENT_SECRET')
        self.redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI')

    def get_access_token(self):
        # Spotify Access Token
        return spotipy.util.prompt_for_user_token(
            username=self.user_id,
            scope=self.scope,
            client_id=self.client_id,
            client_secret=self.client_secret,
            redirect_uri=self.redirect_uri
        )


class Spotify:
    def __init__(self) -> None:
        self.spotify = SpotifyClientManager()

    def create_playlist(self, playlist_name: str) -> str:
        # request_body = {
        #     'name': playlist_name,
        #     'description': 'youtube playlist',
        #     'public': False
        # }

        # query = f"https://api.spotify.com/v1/users/{self.spotify.user_id}/playlists"
        sp = spotipy.Spotify(auth_manager=self.spotify)
        print(sp.current_user_recently_played())


s = Spotify()
s.create_playlist('sdds')
