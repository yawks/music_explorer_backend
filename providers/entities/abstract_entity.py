from abc import ABC, abstractmethod
from json import JSONEncoder
from providers.entities.object_ids import ObjectIds
from providers.objectid_manager import ObjectIdManager


class AbstractEntity(ABC):

    @abstractmethod
    def get_object_ids(self) -> ObjectIds:
        pass

    @abstractmethod
    def merge(self, entity_from_another_provider: "AbstractEntity"):
        self.get_object_ids().merge_provider_object_ids(
            entity_from_another_provider.get_object_ids())


class EntityEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectIds):
            return ObjectIdManager().dumps_list(o)
        return o.__dict__
