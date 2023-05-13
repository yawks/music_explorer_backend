from typing import Optional
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from providers.entities.object_ids import ObjectIds
from providers.spotify.spotify_id import SpotifyId
from providers.spotify.spotify_utils import get_song
from utils.config import Config
from providers.entities.song import Song
from providers.abstract_song_provider import AbstractSongProvider


class SpotifySongProvider(AbstractSongProvider):

    def __init__(self) -> None:
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=Config().get("providers", "spotify", "client_id"),
                                                                client_secret=Config().get("providers", "spotify", "client_secret")))

    def get_song(self, object_ids: ObjectIds) -> Optional[Song]:
        song: Optional[Song] = None
        uri = object_ids.get_id(SpotifyId.get_short_name())
        try:
            track = self.spotify.track(uri)
            if track is not None:
                song = get_song(track)
        except Exception as exception:
            print("Spotify track not found with URI " + ("" if uri is None else uri)+ ": " + str(exception))

        return song

    def get_information(self) -> Optional[str]:
        return None
