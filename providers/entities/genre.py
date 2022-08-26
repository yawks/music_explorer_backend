from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_ids import ObjectIds
from providers.entities.object_id import ObjectId
from typing import List, Optional


class Genre(AbstractEntity):

    def __init__(self, genre_id: ObjectId, name: str, description: str = "") -> None:
        self.genre_ids: ObjectIds = ObjectIds(genre_id)
        self.genre_ids.obj_query_name = name
        self.name: str = name
        self.description: str = description
        self.pictures_url: List[str] = []

    def get_object_ids(self) -> ObjectIds:
        return self.genre_ids

    def merge(self, genre_from_other_provider: "Genre"):
        super().merge(genre_from_other_provider)
        self.pictures_url.extend(genre_from_other_provider.pictures_url)
