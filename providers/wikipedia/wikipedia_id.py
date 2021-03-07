from providers.entities.object_id import ObjectId


class WikipediaId(ObjectId):

    def __init__(self, wikipedia_id: str) -> None:
        super().__init__(wikipedia_id)

    @staticmethod
    def get_short_name() -> str:
        return "wk"
