from providers.spotify.spotify_id import SHORT_NAME
from providers.entities.object_id import ObjectId

SHORT_NAME = "ms"


class MusicStoryId(ObjectId):

    def __init__(self, musicstory_id: str) -> None:
        super().add_provider_id(SHORT_NAME, musicstory_id)

    def get_short_name(self) -> str:
        return SHORT_NAME
