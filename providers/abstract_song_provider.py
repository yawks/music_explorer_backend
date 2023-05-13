from abc import ABC, abstractmethod
from typing import Optional
from providers.entities.object_ids import ObjectIds
from providers.entities.song import Song


class AbstractSongProvider(ABC):
    album: Song

    @abstractmethod
    def get_information(self) -> Optional[str]:
        return None

    @abstractmethod
    def get_song(self, object_ids: ObjectIds) -> Optional[Song]:
        return None
