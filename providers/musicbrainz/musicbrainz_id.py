from providers.entities.object_id import ObjectId


class MusicBrainzId(ObjectId):

    def __init__(self, musicbrainz_id: str) -> None:
        super().__init__(musicbrainz_id)

    @staticmethod
    def get_short_name() -> str:
        return "mb"
