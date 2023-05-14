from providers.spotify.spotify_id import SpotifyId
from providers.entities.playlist import Playlist
from typing import List
from providers.entities.track import Track
from providers.spotify.spotify_playlist_provider import SpotifyPlaylistProvider


def test_search():
    spotify_playlist_provider: SpotifyPlaylistProvider = SpotifyPlaylistProvider(
        playlist=Playlist(
            playlist_id=SpotifyId("37i9dQZF1DXc4xFsxShkAv"),
            name="Led Zeppelin"))

    result: List[Track] = spotify_playlist_provider.get_tracks()
    if len(result) == 0:
        raise AssertionError("result must not be empty")
