from abc import ABC, abstractmethod
from providers.entities.song import Song
from providers.entities.playlist import Playlist
from typing import List, Optional


class AbstractPlaylistProvider(ABC):
    playlist: Playlist

    @abstractmethod
    def get_songs(self) -> List[Song]:
        pass
