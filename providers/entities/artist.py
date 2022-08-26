from providers.entities.object_id import ObjectId
from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_ids import ObjectIds
from typing import List
import Levenshtein


class Artist(AbstractEntity):

    def __init__(self, artist_id: ObjectId, name: str) -> None:
        self.artist_ids: ObjectIds = ObjectIds(artist_id)
        self.name: str = name
        self.artist_ids.obj_query_name = name
        self.pictures_url: List[str] = []

    def get_object_ids(self) -> ObjectIds:
        return self.artist_ids

    def merge(self, artist_from_other_provider: "Artist"):
        super().merge(artist_from_other_provider)
        self.pictures_url.extend(artist_from_other_provider.pictures_url)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Artist):
            return NotImplemented
        other_artist: Artist = other

        return Levenshtein.ratio(self.name, other_artist.name) > 0.7

    def __repr__(self) -> str:
        return "Artist: %s" % self.name
