from utils.singleton import Singleton
import yaml


@Singleton
class Config():

    def __init__(self) -> None:
        with open(r"resources/config.yaml") as file:
            self.yaml = yaml.load(file, Loader=yaml.FullLoader)

    def get(self, *params: str, default_value=None):
        value = default_value

        cur = self.yaml
        cpt: int = 0

        while cpt < len(params):
            param = params[cpt]
            if param in cur:
                cur = cur[param]
            cpt += 1

        if cpt == len(params):
            value = cur

        return value
