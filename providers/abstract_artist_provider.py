from abc import ABC, abstractmethod
from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.song import Song
from providers.entities.artist import Artist
from typing import List, Optional


class AbstractArtistProvider(ABC):
    artist: Artist

    @abstractmethod
    def get_information(self) -> Optional[str]:
        return None

    @abstractmethod
    def get_top_songs(self) -> Optional[List[Song]]:
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