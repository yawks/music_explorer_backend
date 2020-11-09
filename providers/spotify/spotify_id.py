from providers.entities.object_id import ObjectId

SHORT_NAME="sp"

class SpotifyId(ObjectId):

    def __init__(self, spotify_id: str) -> None:
        super().add_provider_id(SHORT_NAME, spotify_id)
    

    def get_short_name(self) -> str:
        return SHORT_NAME
