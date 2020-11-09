from abc import ABC, abstractmethod
from providers.entities.artist_news import ArtistNews
from providers.entities.playlist import Playlist
from providers.entities.album import Album
from providers.entities.genre import Genre
from typing import List, Optional


class AbstractHomeProvider(ABC):

    @abstractmethod
    def get_genres(self) -> Optional[List[Genre]]:
        return None

    @abstractmethod
    def get_new_releases(self) -> Optional[List[Album]]:
        return None

    @abstractmethod
    def get_artists_last_news(self) -> Optional[List[ArtistNews]]:
        return None

    @abstractmethod
    def get_trending_playlists(self) -> Optional[List[Playlist]]:
        return None