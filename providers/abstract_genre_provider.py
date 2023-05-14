from abc import ABC, abstractmethod
from providers.entities.artist_news import ArtistNews
from providers.entities.genre import Genre
from providers.entities.track import Track
from providers.entities.album import Album
from providers.entities.playlist import Playlist
from typing import List, Optional


class AbstractGenreProvider(ABC):
    
    genre: Genre

    @abstractmethod
    def get_information(self) -> Optional[str]:
        return None

    @abstractmethod
    def get_top_tracks(self) -> Optional[List[Track]]:
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