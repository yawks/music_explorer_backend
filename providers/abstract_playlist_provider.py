from abc import ABC, abstractmethod
from providers.entities.track import Track
from providers.entities.playlist import Playlist
from typing import List, Optional


class AbstractPlaylistProvider(ABC):
    playlist: Playlist

    @abstractmethod
    def get_tracks(self) -> List[Track]:
        return []
