from abc import ABC, abstractmethod
from typing import Optional
from providers.entities.object_ids import ObjectIds
from providers.entities.track import Track


class AbstractTrackProvider(ABC):
    album: Track

    @abstractmethod
    def get_information(self) -> Optional[str]:
        return None

    @abstractmethod
    def get_track(self, object_ids: ObjectIds) -> Optional[Track]:
        return None
