from typing import List, Tuple
from providers.entities.album import Album
from providers.entities.genre import Genre
from providers.entities.artist import Artist
from providers.entities.song import Song
from providers.entities.playlist import Playlist
from providers.spotify.spotify_search_provider import SpotifySearchProvider


def test_search():
    spotify_search_provider: SpotifySearchProvider = SpotifySearchProvider()

    result: Tuple[List[Song], List[Artist], List[Album], List[Genre],
                  List[Playlist]] = spotify_search_provider.search("led zeppelin")

    if len(result) == 0:
        raise AssertionError("result must not be empty")
    if len(result[0]) == 0:
        raise AssertionError(
            "spotify search provider should find song results")
    if len(result[1]) == 0:
        raise AssertionError(
            "spotify search provider should find artist results")
    if len(result[2]) == 0:
        raise AssertionError(
            "spotify search provider should find album results")
    if len(result[4]) == 0:
        raise AssertionError(
            "spotify search provider should find playlist results")
