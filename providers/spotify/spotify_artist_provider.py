from typing import List, Optional, cast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils.config import Config
from providers.entities.artist_news import ArtistNews
from providers.entities.object_ids import ObjectId
from providers.spotify.spotify_id import SpotifyId
from providers.spotify.spotify_utils import get_albums, get_artists, get_tracks
from providers.spotify.spotify_provider_information import SpotifyProviderInformation
from providers.entities.album import Album
from providers.entities.track import Track
from providers.entities.artist import Artist
from providers.abstract_artist_provider import AbstractArtistProvider


class SpotifyArtistProvider(AbstractArtistProvider, SpotifyProviderInformation):

    def __init__(self, object_id: ObjectId, name: str) -> None:
        super().__init__(object_id, name)
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=Config().get("providers", "spotify", "client_id"),
                                                                client_secret=Config().get("providers", "spotify", "client_secret")))

    def get_information(self) -> Optional[str]:
        # spotify does not return information about artists (members, biography, ...)
        return None

    def get_top_albums(self) -> Optional[List[Album]]:
        # spotify does not implement this feature
        return None

    def get_similar_artists(self) -> Optional[List[Artist]]:
        artists: dict = cast(
            dict, self.spotify.artist_related_artists(self.object_id))
        return get_artists(artists)

    def get_all_albums(self) -> Optional[List[Album]]:
        albums: dict = cast(dict, self.spotify.artist_albums(self.object_id))
        return get_albums(albums)

    def get_top_tracks(self) -> Optional[List[Track]]:
        tracks: dict = cast(
            dict, self.spotify.artist_top_tracks(self.object_id))
        return get_tracks(tracks)

    def get_news(self) -> Optional[List[ArtistNews]]:
        return None

    def get_artist(self) -> Optional[Artist]:
        """
                a rtists: dict = cast(dict, self.spotify.search(
                    q=artist.name, type="artist"))
                i f "artists" in artists and "items" in artists["artists"]:
                    for item in artists["artists"]["items"]:
                        self.artist_id = item["id"]
                        break
        """
        artist: Optional[Artist] = None
        sp_artist = self.spotify.artist(self.object_id)
        artist = Artist(SpotifyId(sp_artist.get("id")), sp_artist.get("name"))
        if len(sp_artist.get("images")) > 0:
            artist.pictures_url.append(sp_artist.get("images")[0].get("url"))

        return artist
