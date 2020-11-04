from providers.entities.artist import Artist
from typing import List


class ArtistNews():
    title:str
    content: str
    artist: Artist
    pictures_url: List[str]