from typing import List, Optional
import musicbrainzngs
from utils.config import Config
from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.object_ids import ObjectId
from providers.entities.track import Track
from providers.entities.artist import Artist
from providers.abstract_artist_provider import AbstractArtistProvider
from providers.musicbrainz.musicbrainz_provider_information import MusicBrainzProviderInformation


class MusicbrainzArtistProvider(AbstractArtistProvider, MusicBrainzProviderInformation):
    def __init__(self, object_id: ObjectId, name: str) -> None:
        super().__init__(object_id, name)

        musicbrainzngs.set_useragent(
            "python-musicbrainzngs-musicexplorer",
            "0.1",
            "https://github.com/",
        )
        musicbrainzngs.auth(Config().get("providers", "musicbrainz", "login"),
                            Config().get("providers", "musicbrainz", "password"))

    def get_information(self) -> Optional[str]:
        artists = musicbrainzngs.search_artists(
            artist=self.name)

        artist = None
        if "artist-list" in artists and len(artists["artist-list"]) > 0:
            artist = musicbrainzngs.get_artist_by_id(
                artists["artist-list"][0]["id"])

        return artist

    def get_top_tracks(self) -> Optional[List[Track]]:
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
