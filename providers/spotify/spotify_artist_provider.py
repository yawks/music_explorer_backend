from providers.spotify.spotify_utils import get_albums, get_artists, get_songs
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from providers.entities.album import Album
from providers.entities.song import Song
from providers.entities.artist import Artist
from typing import List, Optional, cast
from providers.abstract_artist_provider import AbstractArtistProvider

SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""


class SpotifyArtistProvider(AbstractArtistProvider):
    artist_id: str = ""

    def __init__(self, artist: Artist, language: str = "en") -> None:
        self.artist = artist

        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                                client_secret=SPOTIPY_CLIENT_SECRET))

        artists: dict = cast(dict, self.spotify.search(
            q=artist.name, type="artist"))
        if "artists" in artists and "items" in artists["artists"]:
            for item in artists["artists"]["items"]:
                self.artist_id = item["id"]
                break

    def get_information(self) -> Optional[str]:
        # spotify does not return information about artists (members, biography, ...)
        return None

    def get_top_albums(self) -> Optional[List[Album]]:
        # spotify does not implement this feature
        return None

    def get_similar_artists(self) -> Optional[List[Artist]]:
        artists: dict = cast(
            dict, self.spotify.artist_related_artists(self.artist_id))
        return get_artists(artists)

    def get_all_albums(self) -> Optional[List[Album]]:
        albums: dict = cast(dict, self.spotify.artist_albums(self.artist_id))
        return get_albums(albums)

    def get_top_songs(self) -> Optional[List[Song]]:
        tracks: dict = cast(
            dict, self.spotify.artist_top_tracks(self.artist_id))
        return get_songs(tracks)
