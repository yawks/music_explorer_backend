from abc import ABC, abstractmethod
from providers.entities.artist_news import ArtistNews
from providers.entities.genre import Genre
from providers.entities.song import Song
from providers.entities.album import Album
from providers.entities.playlist import Playlist
from typing import List, Optional


class AbtractGenreProvider(ABC):
    
    genre: Genre

    @abstractmethod
    def get_information(self) -> Optional[str]:
        pass

    @abstractmethod
    def get_top_songs(self) -> Optional[List[Song]]:
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