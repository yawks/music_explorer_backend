import json
from providers.entities.object_id import ObjectId
from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_ids import ObjectIds
from typing import List
from .artist import Artist
import Levenshtein


class Track(AbstractEntity):
    """Track entity

    Args:
        AbstractEntity: generic entity
    """

    def __init__(self, track_id: ObjectId, title: str, artist: Artist, duration: int, stream_url: str = "", external_url: str = "") -> None:
        self.track_ids: ObjectIds = ObjectIds(track_id)
        self.title: str = title
        self.artist: Artist = artist
        self.duration: int = duration
        self.pictures_url: List[str] = []
        self.stream_urls: List[str] = []
        self.external_urls: List[str] = []

        if stream_url != "":
            self.stream_urls.append(stream_url)
        
        if external_url != "":
            self.external_urls.append(external_url)

    def get_object_ids(self) -> ObjectIds:
        return self.track_ids

    def merge(self, entity_from_another_provider: "Track"):
        super().merge(entity_from_another_provider)
        self.pictures_url.extend(entity_from_another_provider.pictures_url)
        self.stream_urls.extend(entity_from_another_provider.stream_urls)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Track):
            return NotImplemented
        same_track: bool = False
        other_track: Track = other
        if Levenshtein.ratio(self.title, other_track.title) > 0.7 \
                and self.artist == other_track.artist:
            same_track = True
        return same_track

    def __repr__(self) -> str:
        return """Track : %s
----
    Artist: %s
    Duration: %ds
    Stream URL: %s

""" % (self.title, str(self.artist), self.duration, self.stream_urls)
