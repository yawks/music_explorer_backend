from utils.singleton import Singleton
import yaml


@Singleton
class Config():

    def __init__(self) -> None:
        with open(r"resources/config.yaml") as file:
            self.yaml = yaml.load(file, Loader=yaml.FullLoader)

    def get(self, *params: str):
        value = None
        cur = self.yaml
        found: bool = True
        for param in params:
            if param in cur:
                cur = cur[param]
            else:
                found = False
                break
        if found:
            value = cur
        return value
