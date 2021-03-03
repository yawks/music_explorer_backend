from providers.youtube.youtube_id import YoutubeId
from providers.entities.playlist import Playlist
from typing import List
from providers.entities.song import Song
from providers.youtube.youtube_playlist_provider import YoutubePlaylistProvider


def test_search():
    youtube_playlist_provider: YoutubePlaylistProvider = YoutubePlaylistProvider(
        playlist=Playlist(
            playlist_id=YoutubeId("VLPL34RkyNxMtmw91urP07awADwtHUEW2fgO"),
            name="Led Zeppelin"))

    result: List[Song] = youtube_playlist_provider.get_songs()
    if len(result) == 0:
        raise AssertionError("result must not be empty")
