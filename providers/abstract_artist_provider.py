from abc import ABC, abstractmethod
from providers.entities.object_ids import ObjectIds
from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.track import Track
from providers.entities.artist import Artist
from typing import List, Optional


class AbstractArtistProvider(ABC):

    def __init__(self, artist_object_ids: ObjectIds) -> None:
        self.artist_object_ids = artist_object_ids

    @abstractmethod
    def get_object_ids(self) -> ObjectIds:
        pass

    @abstractmethod
    def get_information(self) -> Optional[str]:
        return None

    @abstractmethod
    def get_top_tracks(self) -> Optional[List[Track]]:
        return None

    @abstractmethod
    def get_top_albums(self) -> Optional[List[Album]]:
        return None

    @abstractmethod
    def get_all_albums(self) -> Optional[List[Album]]:
        return None

    @abstractmethod
    def get_similar_artists(self) -> Optional[List[Artist]]:
        return None

    @abstractmethod
    def get_news(self) -> Optional[List[ArtistNews]]:
        return None

    @abstractmethod
    def get_artist(self) -> Optional[Artist]:
        return None
