from providers.entities.playlist import Playlist
from providers.spotify.spotify_utils import get_songs
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from providers.entities.song import Song
from providers.abstract_playlist_provider import AbstractPlaylistProvider
from typing import List, cast

SPOTIPY_CLIENT_ID = "2ec23fa3319a45e3b036e588f4848509"
SPOTIPY_CLIENT_SECRET = "516852a0f792479a957944c1bf01e671"


class SpotifyPlaylistProvider(AbstractPlaylistProvider):

    def __init__(self, playlist: Playlist) -> None:
        self.playlist: Playlist = playlist
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                                client_secret=SPOTIPY_CLIENT_SECRET))

    def get_songs(self) -> List[Song]:
        playlist_tracks: dict = cast(dict,
                                     self.spotify.playlist_items(self.playlist.playlist_id))

        return get_songs(playlist_tracks)
