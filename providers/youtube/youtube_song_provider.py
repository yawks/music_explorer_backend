from typing import List, Optional
from ytmusicapi import YTMusic
from providers.entities.object_ids import ObjectIds
from providers.youtube.youtube_id import YoutubeId
from providers.youtube.youtube_utils import convert_duration
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.abstract_track_provider import AbstractTrackProvider


class YoutubeTrackProvider(AbstractTrackProvider):

    def __init__(self) -> None:
        self.ytmusic = YTMusic()

    def get_track(self, object_ids: ObjectIds) -> Optional[Track]:
        track: Optional[Track] = None
        track_id: Optional[str] = object_ids.get_id(
            YoutubeId.get_short_name())
        if track_id is not None:
            result: dict = self.ytmusic.get_song(track_id)
            if "videoDetails" in result:
                track = Track(
                    track_id=YoutubeId(result["videoDetails"]["videoId"]),
                    title=result["videoDetails"]["title"],
                    artist=Artist(
                        artist_id=YoutubeId(""),
                        name=result["videoDetails"]["author"]),
                    duration=convert_duration(
                        result["videoDetails"]["lengthSeconds"]),
                    external_url="https://www.youtube.com/watch?v=" + result["videoDetails"]["videoId"])
                for thumbnail in result["videoDetails"]["thumbnail"]["thumbnails"]:
                    track.pictures_url.append(thumbnail["url"])

        return track

    def get_information(self) -> Optional[str]:
        return super().get_information()
