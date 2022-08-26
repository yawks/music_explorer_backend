from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.object_ids import ObjectIds
from providers.entities.song import Song
from providers.entities.artist import Artist
from typing import List, Optional
import musicbrainzngs
from utils.config import Config
from providers.abstract_artist_provider import AbstractArtistProvider


class MusicbrainzArtistProvider(AbstractArtistProvider):
    def __init__(self, artist_object_ids: ObjectIds) -> None:
        super().__init__(artist_object_ids)

        musicbrainzngs.set_useragent(
            "python-musicbrainzngs-musicexplorer",
            "0.1",
            "https://github.com/",
        )
        musicbrainzngs.auth(Config.instance().get("providers", "musicbrainz", "login"),
                            Config.instance().get("providers", "musicbrainz", "password"))

    def get_object_ids(self) -> ObjectIds:
        return self.artist_object_ids

    def get_information(self) -> Optional[str]:
        artists = musicbrainzngs.search_artists(
            artist=self.artist_object_ids.obj_query_name)

        artist = None
        if "artist-list" in artists and len(artists["artist-list"]) > 0:
            artist = musicbrainzngs.get_artist_by_id(
                artists["artist-list"][0]["id"])

        return artist

    def get_top_songs(self) -> Optional[List[Song]]:
        return None

    def get_all_albums(self) -> Optional[List[Album]]:
        return None

    def get_similar_artists(self) -> Optional[List[Artist]]:
        return None

    def get_top_albums(self) -> Optional[List[Album]]:
        return None

    def get_news(self) -> Optional[List[ArtistNews]]:
        return None

    def get_artist(self) -> Optional[Artist]:
        return None
