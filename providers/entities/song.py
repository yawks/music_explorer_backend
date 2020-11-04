from typing import List
from .artist import Artist


class Song():
    title: str
    artist: Artist
    duration: int
    pictures_url: List[str]
    stream_url: str

    def __init__(self, title: str, artist: Artist, duration: int, stream_url: str = "") -> None:
        self.title = title
        self.artist = artist
        self.duration = duration
        self.pictures_url = []
        self.stream_url = stream_url

    def __repr__(self) -> str:
        return """Song : %s
----
    Artist: %s
    Duration: %ds
    Stream URL: %s

""" % (self.title, str(self.artist), self.duration, self.stream_url)
