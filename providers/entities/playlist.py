from providers.entities.object_id import ObjectId
from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_ids import ObjectIds
from typing import List


class Playlist(AbstractEntity):

    def __init__(self, playlist_id: ObjectId, name: str) -> None:
        self.playlist_ids: ObjectIds = ObjectIds(playlist_id)
        self.playlist_ids.obj_query_name = name
        self.name: str = ""
        self.pictures_url: List[str] = []
        self.name = name

    def get_object_ids(self) -> ObjectIds:
        return self.playlist_ids
    
    def merge(self, playlist_from_other_provider:"Playlist"):
        super().merge(playlist_from_other_provider)
        self.pictures_url.extend(playlist_from_other_provider.pictures_url)

    def __repr__(self) -> str:
        return "Playlist : %s" % self.name
