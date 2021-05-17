from youtube_title_parse import get_artist_title
from googleapiclient.discovery import build
from dataclasses import dataclass
from dotenv import load_dotenv
import os
import prettytable
load_dotenv()


@dataclass
class Song:
    artist: str
    title: str


class Youtube:
    API_KEY = str(os.getenv('API_KEY'))
    API_SERVICE_NAME = "youtube"
    API_VERSION = "v3"

    def __init__(self) -> None:
        self.songs = []
        self.api = build(Youtube.API_SERVICE_NAME,
                         Youtube.API_VERSION, developerKey=Youtube.API_KEY)

    # changed name due to spotify name collison
    def __fetch_songs(self, playList_id, page_token=None):
        result = self.api.playlistItems().list(part="snippet",
                                               playlistId=playList_id,
                                               maxResults="300",
                                               pageToken=page_token
                                               ).execute()

        for item in result['items']:
            songInfo = item['snippet']['title']
            try:
                artist, title = get_artist_title(songInfo)
                self.songs.append(Song(artist, title))
            except:
                print(f'Error parsing {songInfo}')

        return result

    def get_songs_from_playlist(self, playList_id):
        result = self.__fetch_songs(playList_id)
        while 'nextPageToken' in result:
            page_token = result['nextPageToken']
            result = self.__fetch_songs(playList_id, page_token)
        self.printer()

    def printer(self):
        t = prettytable.PrettyTable()
        t.field_names = ['Artist', 'Song']
        for s in self.songs:
            t.add_row([s.artist, s.title])
        print(t)


if __name__ == "__main__":
    yt = Youtube()
    yt.get_songs_from_playlist(
        'PLMC9KNkIncKtPzgY-5rmhvj7fax8fdxoj')
