from typing import List, Tuple
from providers.entities.album import Album
from providers.entities.genre import Genre
from providers.entities.artist import Artist
from providers.entities.song import Song
from providers.entities.playlist import Playlist
from providers.youtube.youtube_search_provider import YoutubeSearchProvider


def test_search():
    youtube_search_provider: YoutubeSearchProvider = YoutubeSearchProvider()

    result: Tuple[List[Song], List[Artist], List[Album], List[Genre],
                  List[Playlist]] = youtube_search_provider.search("led zeppelin")

    if len(result) == 0:
        raise AssertionError("result must not be empty")
