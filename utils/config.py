import yaml


class Config():
    _self = None

    def __init__(self) -> None:
        with open(r"resources/config.yaml") as file:
            self.yaml = yaml.load(file, Loader=yaml.FullLoader)
    
    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

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

    def get_languages(self):
        """Get languages defined in the configuration file, ordered by priority

        Returns:
            _type_: list of language codes (ISO 639-1)
        """
        languages = ["en"]
        config_languages = self.get("lang")
        if isinstance(config_languages, list):
            languages = config_languages

        return languages