from typing import Optional
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from utils.config import Config
from providers.spotify.spotify_provider_information import SpotifyProviderInformation
from providers.spotify.spotify_utils import get_tracks
from providers.abstract_album_provider import AbstractAlbumProvider
from providers.spotify.spotify_id import SpotifyId
from providers.entities.artist import Artist
from providers.entities.object_ids import ObjectIds
from providers.entities.album import Album


class SpotifyAlbumProvider(AbstractAlbumProvider, SpotifyProviderInformation):

    def __init__(self) -> None:
        super().__init__()
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=Config().get("providers", "spotify", "client_id"),
                                                                client_secret=Config().get("providers", "spotify", "client_secret")))

    def get_information(self) -> Optional[str]:
        return None

    def get_album(self, object_ids: ObjectIds) -> Optional[Album]:
        album: Optional[Album] = None
        spotify_id: Optional[str] = object_ids.get_id(
            SpotifyId.get_short_name())
        if spotify_id is not None:
            spotify_album = self.spotify.album(
                spotify_id)
            if "id" in spotify_album and "name" in spotify_album:
                album = Album(
                    album_id=SpotifyId(spotify_album["id"]),
                    name=spotify_album["name"],
                    artist=Artist(
                        artist_id=SpotifyId(spotify_album["artists"][0]["id"]),
                        name=spotify_album["artists"][0]["name"]))
                album.tracks = get_tracks(spotify_album["tracks"])
                for image in spotify_album["images"]:
                    album.pictures_url.append(image["url"])

        return album
