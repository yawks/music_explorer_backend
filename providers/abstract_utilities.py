from abc import ABC, abstractmethod
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.entities.playlist import Playlist
from typing import List, Tuple


class AbstractUtilities(ABC):

    @abstractmethod
    def get_short_name(self) -> str:
        pass
