from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_id import ObjectId
from typing import List
from .song import Song
from .artist import Artist


class Album(AbstractEntity):
    album_id: ObjectId
    name: str
    songs: List[Song]
    artist: Artist
    pictures_url: List[str]

    def __init__(self, album_id: ObjectId, name: str, artist: Artist) -> None:
        self.album_id = album_id
        self.name = name
        self.artist = artist
        self.pictures_url = []
        self.songs = []
    
    def get_object_id(self) -> ObjectId:
        return self.album_id

    def merge(self, album_from_other_provider:"Album"):
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
