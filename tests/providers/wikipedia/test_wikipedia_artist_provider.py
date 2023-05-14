from providers.wikipedia.wikipedia_id import WikipediaId
from typing import Optional
from providers.wikipedia.wikipedia_artist_provider import WikipediaArtistProvider


def test_get_information():
    wikipedia_artist_provider: WikipediaArtistProvider = WikipediaArtistProvider(object_id=WikipediaId("Red Hot Chili Peppers"),
                                                                                 name="Red Hot Chili Peppers")

    information: Optional[str] = wikipedia_artist_provider.get_information()

    if information is None:
        raise AssertionError("information should not be None")
