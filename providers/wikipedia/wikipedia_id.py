from providers.entities.object_id import ObjectId


class WikipediaId(ObjectId):

    @staticmethod
    def get_short_name() -> str:
        return "wk"
