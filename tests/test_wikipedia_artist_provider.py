

from providers.wikipedia.wikipedia_id import WikipediaId
from typing import Optional
from providers.entities.artist import Artist
from providers.wikipedia.wikipedia_artist_provider import WikipediaArtistProvider


def test_get_information():
    musicbrainz_artist_provider: WikipediaArtistProvider = WikipediaArtistProvider(
        artist=Artist(
            artist_id=WikipediaId("dummy"),
            name="Red Hot Chili Peppers"),
        language="fr")

    information: Optional[str] = musicbrainz_artist_provider.get_information()

    if information is None:
        raise AssertionError("information should not be None")
