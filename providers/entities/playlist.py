from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_id import ObjectId
from typing import List


class Playlist(AbstractEntity):

    def __init__(self, playlist_id: ObjectId, name: str) -> None:
        self.playlist_id: ObjectId
        self.name: str = ""
        self.pictures_url: List[str] = []
        self.playlist_id = playlist_id
        self.name = name

    def get_object_id(self) -> ObjectId:
        return self.playlist_id
    
    def merge(self, playlist_from_other_provider:"Playlist"):
        super().merge(playlist_from_other_provider)
        self.pictures_url.extend(playlist_from_other_provider.pictures_url)

    def __repr__(self) -> str:
        return "Playlist : %s" % self.name
