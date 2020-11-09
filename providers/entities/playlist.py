from providers.entities.object_id import ObjectId
from typing import List, Optional


class Playlist():
    playlist_id: ObjectId
    name: str
    pictures_url: List[str]

    def __init__(self, playlist_id: ObjectId, name: str) -> None:
        self.playlist_id = playlist_id
        self.name = name
        self.pictures_url = []
    

    def __repr__(self) -> str:
        return "Playlist : %s" % self.name
