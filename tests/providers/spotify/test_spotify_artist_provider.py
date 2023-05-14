from providers.spotify.spotify_id import SpotifyId
from providers.entities.album import Album
from typing import List, Optional
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.spotify.spotify_artist_provider import SpotifyArtistProvider

TEST_ARTIST_NAME = "led zeppelin"


def test_get_top_tracks():
    spotify_artist_provider: SpotifyArtistProvider = SpotifyArtistProvider(
        artist=Artist(
            artist_id=SpotifyId("dummy"),
            name=TEST_ARTIST_NAME))

    top_tracks: Optional[List[Track]] = spotify_artist_provider.get_top_tracks()

    if top_tracks is None or len(top_tracks) == 0:
        raise AssertionError("led zeppelin has many top tracks!")


def test_get_all_albums():
    spotify_artist_provider: SpotifyArtistProvider = SpotifyArtistProvider(
        artist=Artist(artist_id=SpotifyId("dummy"), name=TEST_ARTIST_NAME))

    albums: Optional[List[Album]] = spotify_artist_provider.get_all_albums()

    if albums is None or len(albums) == 0:
        raise AssertionError("led zeppelin released many albums")


def test_get_similar_artists():
    spotify_artist_provider: SpotifyArtistProvider = SpotifyArtistProvider(
        artist=Artist(artist_id=SpotifyId("dummy"), name=TEST_ARTIST_NAME))

    spotify_artist_provider.get_information()

    artists: Optional[List[Artist]
                      ] = spotify_artist_provider.get_similar_artists()

    if artists is None or len(artists) == 0:
        raise AssertionError("led zeppelin has similar artists")
