from abc import ABC, abstractmethod
from typing import List, Optional
from providers.entities.object_ids import ObjectId
from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.track import Track
from providers.entities.artist import Artist


class AbstractArtistProvider(ABC):

    def __init__(self, object_id: ObjectId, name: str) -> None:
        self.object_id = object_id
        self.name: str = name

    def get_object_id(self) -> ObjectId:
        return self.object_id
    
    def get_name(self) -> str:
        return self.name

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
