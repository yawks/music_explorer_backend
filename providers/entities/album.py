from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_id import ObjectId
from providers.entities.object_ids import ObjectIds
from typing import List
from .track import Track
from .artist import Artist


class Album(AbstractEntity):

    def __init__(self, album_id: ObjectId, name: str, artist: Artist) -> None:
        self.album_ids: ObjectIds = ObjectIds(album_id)
        self.album_ids.obj_query_name = name
        self.name: str = name
        self.artist: Artist = artist
        self.pictures_url: List[str] = []
        self.tracks: List[Track] = []

    def get_object_ids(self) -> ObjectIds:
        return self.album_ids

    def merge(self, album_from_other_provider: "Album"):
        super().merge(album_from_other_provider)
        self.pictures_url.extend(album_from_other_provider.pictures_url)

    def __repr__(self) -> str:
        strtracks: str = ""
        for track in self.tracks:
            strtracks += "\n    " + track.title

        return """Album: %s
-----
    %s
    Tracks:
        %s
""" % (self.name, str(self.artist), strtracks)
