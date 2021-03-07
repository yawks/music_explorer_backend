from abc import ABC, abstractmethod


class ObjectId(ABC):

    def __init__(self, oid: str) -> None:
        self.oid: str = oid

    @staticmethod
    @abstractmethod
    def get_short_name() -> str:
        pass
