from providers.entities.abstract_entity import AbstractEntity
from providers.entities.object_ids import ObjectIds
from providers.entities.artist import Artist
from typing import List


class ArtistNews(AbstractEntity):

    def __init__(self) -> None:
        self.artist_news_id: ObjectIds
        self.title: str = ""
        self.content: str = ""
        self.artist: Artist
        self.pictures_url: List[str] = []

    def get_object_id(self) -> ObjectIds:
        return self.artist_news_id

    def merge(self, artist_news_from_other_provider: "ArtistNews"):
        super().merge(artist_news_from_other_provider)
        self.pictures_url.extend(artist_news_from_other_provider.pictures_url)
