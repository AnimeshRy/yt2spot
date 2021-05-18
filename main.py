from spotify import Spotify
from youtube import Youtube

# utility function for colored output


def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


def main():
    sp = Spotify()
    yt = Youtube()

    yt_playlist_id = input('Enter Youtube Playlist Id: ')
    spotify_playlist_name = input('Name Spotify Playlist: ')
    spotify_playlist_id = sp.create_playlist(spotify_playlist_name)
    songs = yt.get_songs_from_playlist(yt_playlist_id)

    for song in songs:
        song_uri = sp.get_song(song.artist, song.title)

        if not song_uri:
            prRed(f'- {song.artist} - {song.title} was not found')
            continue

        was_added = sp.add_song_to_playlist(spotify_playlist_id, song_uri)

        if was_added:
            prGreen(f'- {song.artist} - {song.title} was added')

    total_songs_added = sp.num_playlist_songs(spotify_playlist_id)
    print(f"Added {total_songs_added} tracks out of {len(songs)}")


if __name__ == "__main__":
    main()
