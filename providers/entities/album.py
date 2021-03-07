from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_id import ObjectId
from providers.entities.object_ids import ObjectIds
from typing import List
from .song import Song
from .artist import Artist


class Album(AbstractEntity):

    def __init__(self, album_id: ObjectId, name: str, artist: Artist) -> None:
        self.album_ids: ObjectIds = ObjectIds(album_id)
        self.name: str = name
        self.artist: Artist = artist
        self.pictures_url: List[str] = []
        self.songs: List[Song] = []

    def get_object_ids(self) -> ObjectIds:
        return self.album_ids

    def merge(self, album_from_other_provider: "Album"):
        super().merge(album_from_other_provider)
        self.pictures_url.extend(album_from_other_provider.pictures_url)

    def __repr__(self) -> str:
        strsongs: str = ""
        for song in self.songs:
            strsongs += "\n    " + song.title

        return """Album: %s
-----
    %s
    Songs:
        %s
""" % (self.name, str(self.artist), strsongs)
