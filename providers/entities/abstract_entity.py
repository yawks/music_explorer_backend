from abc import ABC, abstractmethod
from providers.entities.object_ids import ObjectIds


class AbstractEntity(ABC):

    @abstractmethod
    def get_object_ids(self) -> ObjectIds:
        pass

    @abstractmethod
    def merge(self, entity_from_another_provider: "AbstractEntity"):
        self.get_object_ids().merge_provider_object_ids(
            entity_from_another_provider.get_object_ids())
