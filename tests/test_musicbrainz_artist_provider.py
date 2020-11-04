

from typing import Optional
from providers.entities.artist import Artist
from providers.musicbrainz.musicbrainz_artist_provider import MusicbrainzArtistProvider


def test_get_information():
    musicbrainz_artist_provider: MusicbrainzArtistProvider = MusicbrainzArtistProvider(
        artist=Artist(name="Red Hot Chili Peppers"))

    information: Optional[str] = musicbrainz_artist_provider.get_information()

    if information is None:
        raise AssertionError("information should not be None")
