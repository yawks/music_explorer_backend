from typing import Optional
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils.config import Config
from providers.spotify.spotify_id import SpotifyId
from providers.spotify.spotify_utils import get_track
from providers.spotify.spotify_provider_information import SpotifyProviderInformation
from providers.entities.object_ids import ObjectIds
from providers.entities.track import Track
from providers.abstract_track_provider import AbstractTrackProvider


class SpotifyTrackProvider(AbstractTrackProvider, SpotifyProviderInformation):

    def __init__(self) -> None:
        super().__init__()
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=Config().get("providers", "spotify", "client_id"),
                                                                client_secret=Config().get("providers", "spotify", "client_secret")))

    def get_track(self, object_ids: ObjectIds) -> Optional[Track]:
        track: Optional[Track] = None
        uri = object_ids.get_id(SpotifyId.get_short_name())
        try:
            track = self.spotify.track(uri)
            if track is not None:
                track = get_track(track)
        except Exception as exception:
            print("Spotify track not found with URI " + ("" if uri is None else uri)+ ": " + str(exception))

        return track

    def get_information(self) -> Optional[str]:
        return None
