from typing import List, Optional
from ytmusicapi import YTMusic
from providers.entities.object_ids import ObjectIds
from providers.youtube.youtube_id import YoutubeId
from providers.youtube.youtube_utils import convert_duration
from providers.entities.artist import Artist
from providers.entities.song import Song
from providers.abstract_song_provider import AbstractSongProvider


class YoutubeSongProvider(AbstractSongProvider):

    def __init__(self) -> None:
        self.ytmusic = YTMusic()

    def get_song(self, object_ids: ObjectIds) -> Optional[Song]:
        song: Optional[Song] = None
        song_id: Optional[str] = object_ids.get_id(
            YoutubeId.get_short_name())
        if song_id is not None:
            result: dict = self.ytmusic.get_song(song_id)
            if "videoDetails" in result:
                song = Song(
                    song_id=YoutubeId(result["videoDetails"]["videoId"]),
                    title=result["videoDetails"]["title"],
                    artist=Artist(
                        artist_id=YoutubeId(""),
                        name=result["videoDetails"]["author"]),
                    duration=convert_duration(
                        result["videoDetails"]["lengthSeconds"]),
                    external_url="https://www.youtube.com/watch?v=" + result["videoDetails"]["videoId"])
                for thumbnail in result["videoDetails"]["thumbnail"]["thumbnails"]:
                    song.pictures_url.append(thumbnail["url"])

        return song

    def get_information(self) -> Optional[str]:
        return super().get_information()
