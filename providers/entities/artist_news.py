from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_id import ObjectId
from providers.entities.artist import Artist
from typing import List


class ArtistNews(AbstractEntity):

    def __init__(self) -> None:
        self.artist_news_id: ObjectId
        self.title: str = ""
        self.content: str = ""
        self.artist: Artist
        self.pictures_url: List[str] = []

    def get_object_id(self) -> ObjectId:
        return self.artist_news_id

    def merge(self, artist_news_from_other_provider: "ArtistNews"):
        super().merge(artist_news_from_other_provider)
        self.pictures_url.extend(artist_news_from_other_provider.pictures_url)
