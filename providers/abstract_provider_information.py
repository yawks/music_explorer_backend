from abc import ABC

class AbstractProviderInformation(ABC):

    def __init__(self, name: str, icon: str) -> None:
        super().__init__()
        self.name: str = name
        self.icon: str = icon

    def get_provider_information(self) -> dict:
        return {
            "name" : self.name,
            "icon" : self.icon
        }
