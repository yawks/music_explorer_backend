from abc import ABC, abstractmethod
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.entities.playlist import Playlist
from typing import List, Tuple


class AbstractSearchProvider(ABC):
    @abstractmethod
    def search(self, query: str) -> Tuple[List[Track], List[Artist], List[Album], List[Genre], List[Playlist]]:
        return []

    @abstractmethod
    def search_track(self, query: str) -> List[Track]:
        return []

    @abstractmethod
    def search_artist(self, query: str) -> List[Artist]:
        return []

    @abstractmethod
    def search_album(self, query: str) -> List[Album]:
        return []

    @abstractmethod
    def search_genre(self, query: str) -> List[Genre]:
        return []

    @abstractmethod
    def search_playlist(self, query: str) -> List[Playlist]:
        return []
