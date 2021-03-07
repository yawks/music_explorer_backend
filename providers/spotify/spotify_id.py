from providers.entities.object_id import ObjectId


class SpotifyId(ObjectId):

    def __init__(self, spotify_id: str) -> None:
        super().__init__(spotify_id)

    @staticmethod
    def get_short_name() -> str:
        return "sp"
