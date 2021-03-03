from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_id import ObjectId
from typing import List


class Genre(AbstractEntity):

    def __init__(self) -> None:
        self.genre_id: ObjectId
        self.name: str = ""
        self.description: str = ""
        self.pictures_url: List[str] = []

    def get_object_id(self) -> ObjectId:
        return self.genre_id
    
    def merge(self, genre_from_other_provider:"Genre"):
        super().merge(genre_from_other_provider)
        self.pictures_url.extend(genre_from_other_provider.pictures_url)
