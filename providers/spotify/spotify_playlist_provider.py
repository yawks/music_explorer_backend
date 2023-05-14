from typing import List, cast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils.config import Config
from providers.entities.playlist import Playlist
from providers.spotify.spotify_id import SpotifyId
from providers.spotify.spotify_utils import get_tracks
from providers.entities.track import Track
from providers.abstract_playlist_provider import AbstractPlaylistProvider
from providers.spotify.spotify_provider_information import SpotifyProviderInformation


class SpotifyPlaylistProvider(AbstractPlaylistProvider, SpotifyProviderInformation):

    def __init__(self, playlist: Playlist) -> None:
        super().__init__()
        self.playlist: Playlist = playlist
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=Config().get("providers", "spotify", "client_id"),
                                                                client_secret=Config().get("providers", "spotify", "client_secret")))

    def get_tracks(self) -> List[Track]:
        playlist_tracks: dict = cast(dict,
                                     self.spotify.playlist_items(self.playlist.get_object_ids().get_id(SpotifyId.get_short_name())))

        return get_tracks(playlist_tracks)
