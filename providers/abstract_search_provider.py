from abc import ABC, abstractmethod
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.song import Song
from providers.entities.playlist import Playlist
from typing import List, Tuple


class AbstractSearchProvider(ABC):
    @abstractmethod
    def search(self, query: str) -> Tuple[List[Song], List[Artist], List[Album], List[Genre], List[Playlist]]:
        pass

    @abstractmethod
    def search_song(self, query: str) -> List[Song]:
        pass

    @abstractmethod
    def search_artist(self, query: str) -> List[Artist]:
        pass

    @abstractmethod
    def search_album(self, query: str) -> List[Album]:
        pass

    @abstractmethod
    def search_genre(self, query: str) -> List[Genre]:
        pass

    @abstractmethod
    def search_playlist(self, query: str) -> List[Playlist]:
        pass
