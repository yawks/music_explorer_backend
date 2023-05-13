from providers.entities.artist_news import ArtistNews
from providers.entities.object_ids import ObjectIds
from providers.spotify.spotify_id import SpotifyId
from utils.config import Config
from providers.spotify.spotify_utils import get_albums, get_artists, get_songs
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from providers.entities.album import Album
from providers.entities.song import Song
from providers.entities.artist import Artist
from typing import List, Optional, cast
from providers.abstract_artist_provider import AbstractArtistProvider


class SpotifyArtistProvider(AbstractArtistProvider):

    def __init__(self, artist_object_ids: ObjectIds) -> None:
        super().__init__(artist_object_ids)
        self.spotify = spotipy.Spotify(
            client_credentials_manager=SpotifyClientCredentials(client_id=Config().get("providers", "spotify", "client_id"),
                                                                client_secret=Config().get("providers", "spotify", "client_secret")))

    def get_object_ids(self) -> ObjectIds:
        return self.artist_object_ids

    def get_information(self) -> Optional[str]:
        # spotify does not return information about artists (members, biography, ...)
        return None

    def get_top_albums(self) -> Optional[List[Album]]:
        # spotify does not implement this feature
        return None

    def get_similar_artists(self) -> Optional[List[Artist]]:
        artists: dict = cast(
            dict, self.spotify.artist_related_artists(self.artist_object_ids.get_id(SpotifyId.get_short_name())))
        return get_artists(artists)

    def get_all_albums(self) -> Optional[List[Album]]:
        albums: dict = cast(dict, self.spotify.artist_albums(
            self.artist_object_ids.get_id(SpotifyId.get_short_name())))
        return get_albums(albums)

    def get_top_songs(self) -> Optional[List[Song]]:
        tracks: dict = cast(
            dict, self.spotify.artist_top_tracks(self.artist_object_ids.get_id(SpotifyId.get_short_name())))
        return get_songs(tracks)

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
        sp_artist = self.spotify.artist(
            self.artist_object_ids.get_id(SpotifyId.get_short_name()))
        artist = Artist(SpotifyId(sp_artist.get("id")), sp_artist.get("name"))
        if len(sp_artist.get("images")) > 0:
            artist.pictures_url.append(sp_artist.get("images")[0].get("url"))

        return artist
