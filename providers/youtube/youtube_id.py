from providers.entities.object_id import ObjectId


class YoutubeId(ObjectId):

    def __init__(self, youtube_id: str) -> None:
        super().__init__(youtube_id)

    @staticmethod
    def get_short_name() -> str:
        return "yt"
