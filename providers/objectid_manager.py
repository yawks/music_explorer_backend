from glob import glob
import importlib
import inspect
import os
from base64 import b64encode, b64decode
from ast import literal_eval
from typing import Dict, Optional, Tuple, Union
import jsons
from providers.entities.object_ids import ObjectIds
from providers.entities.object_id import ObjectId


class ObjectIdManager():
    _self = None
    object_ids: dict = {}

    def __init__(self) -> None:
        for directory in glob("providers/*"):
            if os.path.isdir(directory):
                self._load_providers(directory)

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def _load_providers(self, directory: str):
        for provider_path in glob(f"{directory}/*.py"):
            if provider_path.strip(directory) != "__init__.py":
                module_name, package_name = self._get_module_and_package_name(
                    provider_path)

                module = importlib.import_module(
                    module_name, package=package_name)
                self._search_for_objectid_classes(module)

    def _search_for_objectid_classes(self, module):
        for abstract_provider in ["ObjectId"]:
            if hasattr(module, abstract_provider):
                for member in inspect.getmembers(module):
                    self._load_objectid_module(
                        abstract_provider, module, member)

    def _get_module_and_package_name(self, provider_path: str) -> Tuple[str, str]:
        module_name: str = "." + os.path.basename(provider_path)
        package_name: str = os.path.dirname(
            provider_path).replace(os.path.sep, ".")

        thelen = len(".py")
        if module_name[-thelen:] == ".py":
            module_name = module_name[:-thelen]

        return (module_name, package_name)

    def _load_objectid_module(self, abstract_objectid: str, module, objectid_class):
        if objectid_class[0].find("__") == -1 \
                and isinstance(objectid_class[1], type) \
                and issubclass(objectid_class[1], getattr(module, abstract_objectid, "")) \
                and objectid_class[1].__name__ != abstract_objectid:

            object_id: ObjectId = objectid_class[1]("")

            self.object_ids[object_id.get_short_name()] = objectid_class[1]

    def get_objectid_by_name(self, objectid_name: str, objectid_id: str) -> Optional[ObjectId]:
        object_id: Optional[ObjectId] = None
        if objectid_name in self.object_ids:
            object_id = self.object_ids[objectid_name](objectid_id)

        return object_id

    def dumps(self, object_id: ObjectId) -> str:
        return b64encode(jsons.dumps({object_id.get_short_name(): object_id.oid}).encode("ASCII")).decode("ASCII")

    def dumps_list(self, object_ids: ObjectIds) -> str:
        oids_encodable: Dict[str, str] = {}
        oids_encodable["obj_query_name"] = object_ids.obj_query_name
        for short_name, object_id in object_ids.object_id_dict.items():
            oids_encodable[short_name] = object_id.oid
        return b64encode(jsons.dumps(oids_encodable).encode("ASCII")).decode("ASCII")

    def loads(self, encoded: str) -> ObjectIds:
        object_ids: ObjectIds = ObjectIds()
        json = literal_eval(
            b64decode(encoded.encode("ASCII")).decode("ASCII"))
        object_ids.obj_query_name = json.get("obj_query_name")
        for oid_name in json:
            oid: Optional[ObjectId] = self.get_objectid_by_name(
                oid_name, json[oid_name])
            if oid is not None:
                object_ids.add_provider_object_id(oid)

        return object_ids


def object_id_serializer(object_ids: ObjectIds, **_) -> Union[int, str]:
    return ObjectIdManager().dumps_list(object_ids)
