

from providers.musicbrainz.musicbrainz_id import MusicBrainzId
from typing import Optional
from providers.entities.artist import Artist
from providers.musicbrainz.musicbrainz_artist_provider import MusicbrainzArtistProvider

ARTIST_NAME = "Red Hot Chili Peppers"

def test_get_information():
    musicbrainz_artist_provider: MusicbrainzArtistProvider = MusicbrainzArtistProvider(
            object_id=MusicBrainzId("dummy"),
            name=ARTIST_NAME)
    
    information: Optional[str] = musicbrainz_artist_provider.get_information()

    if information is None:
        raise AssertionError("information should not be None")
