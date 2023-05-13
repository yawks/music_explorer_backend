import json
from providers.entities.object_id import ObjectId
from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_ids import ObjectIds
from typing import List
from .artist import Artist
import Levenshtein


class Song(AbstractEntity):
    """Song entity

    Args:
        AbstractEntity: generic entity
    """

    def __init__(self, song_id: ObjectId, title: str, artist: Artist, duration: int, stream_url: str = "") -> None:
        self.song_ids: ObjectIds = ObjectIds(song_id)
        self.title: str = title
        self.artist: Artist = artist
        self.duration: int = duration
        self.pictures_url: List[str] = []
        self.stream_urls: List[str] = [stream_url]

    def get_object_ids(self) -> ObjectIds:
        return self.song_ids

    def merge(self, entity_from_another_provider: "Song"):
        super().merge(entity_from_another_provider)
        self.pictures_url.extend(entity_from_another_provider.pictures_url)
        self.stream_urls.extend(entity_from_another_provider.stream_urls)

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

""" % (self.title, str(self.artist), self.duration, self.stream_urls)
