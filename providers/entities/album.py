from providers.entities.object_id import ObjectId
from typing import List
from .song import Song
from .artist import Artist


class Album():
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
