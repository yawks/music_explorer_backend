from typing import List, Tuple
from providers.entities.album import Album
from providers.entities.genre import Genre
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.entities.playlist import Playlist
from providers.providers_manager import ProviderManager


def test_search_providers():
    search_providers: list = ProviderManager().get_search_providers()
    assert len(search_providers) > 0

    search_provider_class = search_providers[-1]
    search_provider = search_provider_class()

    result: Tuple[List[Track], List[Artist], List[Album], List[Genre],
                  List[Playlist]] = search_provider.search("led zeppelin")

    assert len(result[0]) > 0
