from typing import List
from .song import Song
from .artist import Artist


class Album():
    name: str
    songs: List[Song]
    artist: Artist
    pictures_url: List[str]

    def __init__(self, name: str, artist: Artist) -> None:
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
