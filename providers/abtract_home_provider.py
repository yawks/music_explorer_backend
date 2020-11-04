from abc import ABC, abstractmethod
from providers.entities.artist_news import ArtistNews
from providers.entities.playlist import Playlist
from providers.entities.album import Album
from providers.entities.genre import Genre
from typing import List, Optional


class AbtractHomeProvider(ABC):

    @abstractmethod
    def get_genres(self) -> Optional[List[Genre]]:
        pass

    @abstractmethod
    def get_new_releases(self) -> Optional[List[Album]]:
        pass

    @abstractmethod
    def get_artists_last_news(self) -> Optional[List[ArtistNews]]:
        pass

    @abstractmethod
    def get_trending_playlists(self) -> Optional[List[Playlist]]:
        pass