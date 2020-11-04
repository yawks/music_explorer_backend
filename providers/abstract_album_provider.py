from abc import ABC, abstractmethod
from providers.entities.album import Album
from typing import Optional


class AbstractAlbumProvider(ABC):
    album: Album

    @abstractmethod
    def get_information(self) -> Optional[str]:
        pass