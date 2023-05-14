from typing import List, Optional
from providers.spotify.spotify_id import SpotifyId
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.spotify.spotify_artist_provider import SpotifyArtistProvider

TEST_ARTIST_NAME = "led zeppelin"

def _get_spotify_artist_provider():
    return SpotifyArtistProvider(
        object_id=SpotifyId("dummy"),
            name=TEST_ARTIST_NAME)

def test_get_top_tracks():
    spotify_artist_provider: SpotifyArtistProvider = _get_spotify_artist_provider()

    top_tracks: Optional[List[Track]] = spotify_artist_provider.get_top_tracks()

    if top_tracks is None or len(top_tracks) == 0:
        raise AssertionError("led zeppelin has many top tracks!")


def test_get_all_albums():
    spotify_artist_provider: SpotifyArtistProvider = _get_spotify_artist_provider()

    albums: Optional[List[Album]] = spotify_artist_provider.get_all_albums()

    if albums is None or len(albums) == 0:
        raise AssertionError("led zeppelin released many albums")


def test_get_similar_artists():
    spotify_artist_provider: SpotifyArtistProvider = _get_spotify_artist_provider()

    spotify_artist_provider.get_information()

    artists: Optional[List[Artist]
                      ] = spotify_artist_provider.get_similar_artists()

    if artists is None or len(artists) == 0:
        raise AssertionError("led zeppelin has similar artists")
