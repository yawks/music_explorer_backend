from abc import ABC, abstractmethod
from providers.entities.album import Album
from providers.entities.song import Song
from providers.entities.artist import Artist
from typing import List, Optional


class AbstractArtistProvider(ABC):
    artist: Artist

    @abstractmethod
    def get_information(self) -> Optional[str]:
        pass

    @abstractmethod
    def get_top_songs(self) -> Optional[List[Song]]:
        pass

    @abstractmethod
    def get_top_albums(self) -> Optional[List[Album]]:
        pass

    @abstractmethod
    def get_all_albums(self) -> Optional[List[Album]]:
        pass

    @abstractmethod
    def get_similar_artists(self) -> Optional[List[Artist]]:
        pass