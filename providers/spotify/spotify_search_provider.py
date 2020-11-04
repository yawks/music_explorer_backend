from providers.spotify.spotify_utils import get_albums, get_artists, get_playlists, get_songs
from spotipy.oauth2 import SpotifyClientCredentials
from providers.abstract_search_provider import AbstractSearchProvider
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.song import Song
from providers.entities.playlist import Playlist
from typing import List, Tuple, cast
import spotipy


SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""


class SpotifySearchProvider(AbstractSearchProvider):

    def __init__(self) -> None:
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                                client_secret=SPOTIPY_CLIENT_SECRET))

    def search(self, query: str) -> Tuple[List[Song], List[Artist], List[Album], List[Genre], List[Playlist]]:
        songs: List[Song] = []
        artists: List[Artist] = []
        albums: List[Album] = []
        genres: List[Genre] = []
        playlists: List[Playlist] = []

        results = self.spotify.search(
            q=query, type="artist,album,track,playlist")

        albums = get_albums(results["albums"])
        artists = get_artists(results["artists"])
        songs = get_songs(results["tracks"])
        playlists = get_playlists(results["playlists"])

        return (songs, artists, albums, genres, playlists)

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

    def search_song(self, query: str) -> List[Song]:
        return []
