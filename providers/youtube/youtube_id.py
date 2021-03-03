from providers.spotify.spotify_id import SHORT_NAME
from providers.entities.object_id import ObjectId

SHORT_NAME = "yt"


class YoutubeId(ObjectId):

    def __init__(self, youtube_id: str) -> None:
        super().__init__()
        super().add_provider_id(SHORT_NAME, youtube_id)

    def get_short_name(self) -> str:
        return SHORT_NAME
