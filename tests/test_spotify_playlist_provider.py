from providers.entities.playlist import Playlist
from typing import List
from providers.entities.song import Song
from providers.spotify.spotify_playlist_provider import SpotifyPlaylistProvider


def test_search():
    spotify_playlist_provider: SpotifyPlaylistProvider = SpotifyPlaylistProvider(
        playlist=Playlist(name="Led Zeppelin", playlist_id="37i9dQZF1DXc4xFsxShkAv"))

    result: List[Song] = spotify_playlist_provider.get_songs()
    if len(result) == 0:
        raise AssertionError("result must not be empty")
