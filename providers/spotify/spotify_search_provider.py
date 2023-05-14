from typing import List, Tuple
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils.config import Config
from providers.spotify.spotify_utils import get_albums, get_artists, get_playlists, get_tracks
from providers.spotify.spotify_provider_information import SpotifyProviderInformation
from providers.abstract_search_provider import AbstractSearchProvider
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.entities.playlist import Playlist


class SpotifySearchProvider(AbstractSearchProvider, SpotifyProviderInformation):

    def __init__(self) -> None:
        super().__init__()
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=Config().get("providers", "spotify", "client_id"),
                                                                client_secret=Config().get("providers", "spotify", "client_secret")))

    def search(self, query: str) -> Tuple[List[Track], List[Artist], List[Album], List[Genre], List[Playlist]]:
        tracks: List[Track] = []
        artists: List[Artist] = []
        albums: List[Album] = []
        genres: List[Genre] = []
        playlists: List[Playlist] = []

        results = self.spotify.search(
            q=query, type="artist,album,track,playlist")

        albums = get_albums(results["albums"])
        artists = get_artists(results["artists"])
        tracks = get_tracks(results["tracks"])
        playlists = get_playlists(results["playlists"])

        return (tracks, artists, albums, genres, playlists)

    def search_album(self, query: str) -> List[Album]:
        results = self.spotify.search(
            q=query, type="album")

        return get_albums(results["albums"])

    def search_artist(self, query: str) -> List[Artist]:
        results = self.spotify.search(
            q=query, type="artist")

        return get_artists(results["artists"])

    def search_genre(self, query: str) -> List[Genre]:
        return []

    def search_playlist(self, query: str) -> List[Playlist]:
        results = self.spotify.search(
            q=query, type="playlist")
        return get_playlists(results["playlists"])

    def search_track(self, query: str) -> List[Track]:
        return []
