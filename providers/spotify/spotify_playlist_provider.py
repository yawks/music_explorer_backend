from utils.config import Config
from providers.entities.playlist import Playlist
from providers.spotify.spotify_id import SpotifyId
from providers.spotify.spotify_utils import get_songs
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from providers.entities.song import Song
from providers.abstract_playlist_provider import AbstractPlaylistProvider
from typing import List, cast


class SpotifyPlaylistProvider(AbstractPlaylistProvider):

    def __init__(self, playlist: Playlist) -> None:
        self.playlist: Playlist = playlist
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=Config().get("providers", "spotify", "client_id"),
                                                                client_secret=Config().get("providers", "spotify", "client_secret")))

    def get_songs(self) -> List[Song]:
        playlist_tracks: dict = cast(dict,
                                     self.spotify.playlist_items(self.playlist.get_object_ids().get_id(SpotifyId.get_short_name())))

        return get_songs(playlist_tracks)
