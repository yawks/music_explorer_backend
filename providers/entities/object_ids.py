from abc import ABC
from typing import Dict, Optional
from providers.entities.object_id import ObjectId


class ObjectIds(ABC):

    def __init__(self, object_id: Optional[ObjectId] = None) -> None:
        self.object_id_dict: Dict[str, ObjectId] = {}
        self.obj_query_name: str = ""
        if object_id is not None:
            self.object_id_dict[object_id.get_short_name()] = object_id

    def add_provider_object_id(self, other_provider_object_id: ObjectId):
        self.object_id_dict[other_provider_object_id.get_short_name()
                        ] = other_provider_object_id

    def merge_provider_object_ids(self, other_provider_object_ids: "ObjectIds"):
        for short_name, object_id in other_provider_object_ids.object_id_dict.items():
            if short_name not in self.object_id_dict:
                self.object_id_dict[short_name] = object_id

    def get_id(self, short_name) -> Optional[str]:
        oid: Optional[str] = None

        if short_name in self.object_id_dict:
            oid = self.object_id_dict[short_name].oid

        return oid

    def __repr__(self) -> str:
        _repr_: str = ""

        for short_name, object_id in self.object_id_dict.items():
            _repr_ += "[%s:%s] " % (short_name,
                                    object_id.oid)

        return _repr_
