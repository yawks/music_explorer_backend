from abc import ABC, abstractmethod
from providers.entities.object_id import ObjectId


class AbstractEntity(ABC):

    @abstractmethod
    def get_object_id(self) -> ObjectId:
        pass

    @abstractmethod
    def merge(self, entity_from_another_provider: "AbstractEntity"):
        self.get_object_id().merge_provider(entity_from_another_provider.get_object_id())
