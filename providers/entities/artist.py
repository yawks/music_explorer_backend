from typing import List


class Artist():
    name: str
    pictures_url: List[str]

    def __init__(self, name: str) -> None:
        self.name = name
        self.pictures_url = []
    

    def __repr__(self) -> str:
        return "Artist: %s" % self.name
