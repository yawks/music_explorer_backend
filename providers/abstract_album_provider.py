from abc import ABC, abstractmethod
from providers.entities.object_ids import ObjectIds
from providers.entities.object_id import ObjectId
from providers.entities.album import Album
from typing import Optional


class AbstractAlbumProvider(ABC):
    album: Album

    @abstractmethod
    def get_information(self) -> Optional[str]:
        return None

    @abstractmethod
    def get_album(self, id: ObjectIds) -> Optional[Album]:
        return None
