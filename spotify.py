import os
import spotipy
import dotenv
dotenv.load_dotenv()


class SpotifyClientManager:
    def __init__(self) -> None:
        self.scope = 'playlist-modify-public'
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
        self.sp = spotipy.Spotify(auth_manager=self.spotify)

    def create_playlist(self, playlist_name: str) -> str:
        # create a public playlist for the user

        playlist = self.sp.user_playlist_create(user=os.getenv(
            'SPOTIFY_USER_ID'), name=playlist_name, public=True)
        return str(playlist['id'])

    def get_song(self, artist: str, song_name: str) -> str:
        # retrieve Song URI

        q = f'artist:{artist} track:{song_name}'
        try:
            results = self.sp.search(q, limit=1, type='track')
        except:
            print(f"Error retrieving {song_name} by {artist}")
            return None

        items = results["tracks"]["items"]
        if not items:
            return None
        else:
            return items[0]["uri"]

    def add_song_to_playlist(self, playlist_id: str, song_uri: str) -> bool:
        # add song to playlist based on URI provided
        try:
            res = self.sp.playlist_add_items(
                playlist_id=playlist_id, items=[song_uri])
            return True
        except:
            return False

    def num_playlist_songs(self, playlist_id: str) -> int:
        try:
            res = self.sp.playlist_tracks(playlist_id)
        except:
            return None
        return int(res['total'])


if __name__ == "__main__":
    s = Spotify()
    p_id = s.create_playlist('Test-Playlist')
    print(p_id)
    s_uri = s.get_song('Justin Bieber', 'Peaches ft. Daniel Caesar, Giveon')
    print(s.add_song_to_playlist(p_id, [s_uri]))
    print(s.num_playlist_songs(p_id))
