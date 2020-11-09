from providers.entities.object_id import ObjectId
from typing import List


class Artist():
    artist_id: ObjectId
    name: str
    pictures_url: List[str]

    def __init__(self, artist_id: ObjectId, name: str) -> None:
        self.artist_id = artist_id
        self.name = name
        self.pictures_url = []

    def __repr__(self) -> str:
        return "Artist: %s" % self.name
