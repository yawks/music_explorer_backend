from abc import ABC, abstractmethod
from base64 import b64encode, b64decode
from typing import Dict, Optional
from ast import literal_eval


class ObjectId(ABC):
    """Each entity can have multiple IDs from different providers.
       ObjectId is a way to keep them all in a single object with serialization unserialization feature.

    Returns:
        [type]: [description]
    """
    providers_id: Dict[str, str] = {}

    def __init__(self, provider_short_name: str = "", object_id: str = "") -> None:
        if provider_short_name != "":
            self.add_provider_id(provider_short_name, object_id)

    def add_provider_id(self, provider_short_name: str, object_id: str):
        self.providers_id[provider_short_name] = object_id

    def dumps(self) -> str:
        return b64encode(str(self.providers_id).encode("ASCII")).decode("ASCII")

    def loads(self, encoded: str):
        self.providers_id = literal_eval(
            b64decode(encoded.encode("ASCII")).decode("ASCII"))
    
    def get_id(self) -> Optional[str]:
        object_id: Optional[str] = None
        if self.get_short_name() in self.providers_id:
            object_id = self.providers_id[self.get_short_name()]
        return object_id

    @abstractmethod
    def get_short_name(self) -> str:
        pass

