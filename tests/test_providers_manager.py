from providers.abstract_search_provider import AbstractSearchProvider
from typing import List, Tuple, cast
from providers.entities.album import Album
from providers.entities.genre import Genre
from providers.entities.artist import Artist
from providers.entities.song import Song
from providers.entities.playlist import Playlist
from providers.providers_manager import ProviderManager


def test_search_providers():
    search_providers: list = ProviderManager.instance().get_search_providers()
    assert len(search_providers) > 0

    search_provider_class: AbstractSearchProvider = cast(AbstractSearchProvider, search_providers[0])
    search_provider = search_provider_class()

    result: Tuple[List[Song], List[Artist], List[Album], List[Genre],
                  List[Playlist]] = saerch_provider.search("led zeppelin")
    
    result = result
    
