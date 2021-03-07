from providers.entities.object_id import ObjectId

class MusicStoryId(ObjectId):

    def __init__(self, musicstory_id: str) -> None:
        super().__init__(musicstory_id)

    @staticmethod
    def get_short_name() -> str:
        return "ms"
