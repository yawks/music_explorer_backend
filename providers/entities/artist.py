from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_id import ObjectId
from typing import List
import Levenshtein


class Artist(AbstractEntity):
    

    def __init__(self, artist_id: ObjectId, name: str) -> None:
        self.artist_id: ObjectId
        self.name: str
        self.pictures_url: List[str]
        self.artist_id = artist_id
        self.name = name
        self.pictures_url = []
    
    def get_object_id(self) -> ObjectId:
        return self.artist_id
    
    def merge(self, artist_from_other_provider:"Artist"):
        super().merge(artist_from_other_provider)
        self.pictures_url.extend(artist_from_other_provider.pictures_url)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Artist):
            return NotImplemented
        other_artist: Artist = other

        return Levenshtein.ratio(self.name, other_artist.name) > 0.7

    def __repr__(self) -> str:
        return "Artist: %s" % self.name
