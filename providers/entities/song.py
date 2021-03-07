from providers.entities.object_id import ObjectId
from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_ids import ObjectIds
from typing import List
from .artist import Artist
import Levenshtein


class Song(AbstractEntity):

    def __init__(self, song_id: ObjectId, title: str, artist: Artist, duration: int, stream_url: str = "") -> None:
        self.song_ids: ObjectIds = ObjectIds(song_id)
        self.title: str = title
        self.artist: Artist = artist
        self.duration: int = duration
        self.pictures_url: List[str] = []
        self.stream_url: List[str] = [stream_url]

    def get_object_ids(self) -> ObjectIds:
        return self.song_ids

    def merge(self, song_from_other_provider: "Song"):
        super().merge(song_from_other_provider)
        self.pictures_url.extend(song_from_other_provider.pictures_url)
        self.stream_url.extend(song_from_other_provider.stream_url)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Song):
            return NotImplemented
        same_song: bool = False
        other_song: Song = other
        if Levenshtein.ratio(self.title, other_song.title) > 0.7 \
                and self.artist == other_song.artist:
            same_song = True
        return same_song

    def __repr__(self) -> str:
        return """Song : %s
----
    Artist: %s
    Duration: %ds
    Stream URL: %s

""" % (self.title, str(self.artist), self.duration, self.stream_url)
