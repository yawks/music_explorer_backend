from typing import Any, List, Optional
from threading import Thread
from enum import Enum
from providers.entities.object_ids import ObjectIds
from providers.entities import artist
from providers.abstract_artist_provider import AbstractArtistProvider
from providers.providers_manager import ProviderManager


class ArtistQueryType(Enum):
    ARTIST = 1
    INFO = 2
    NEWS = 3


class ArtistHandler():

    def __init__(self, artist_ids: ObjectIds, query_type: ArtistQueryType) -> None:
        self.artist_ids: ObjectIds = artist_ids
        self.artist_provider_threads: List[AbstractArtistThread] = []
        threads: list = []

        for artist_provider_class in ProviderManager.instance().get_artist_providers():
            artist_provider_object = artist_provider_class(artist_ids)
            if query_type == ArtistQueryType.NEWS:
                artist_thread: AbstractArtistThread = ArtistNewsThread(
                    artist_provider_object)
            elif query_type == ArtistQueryType.INFO:
                artist_thread: AbstractArtistThread = ArtistInformationThread(
                    artist_provider_object)
            else:
                artist_thread: AbstractArtistThread = ArtistProviderThread(
                    artist_provider_object)

            self.artist_provider_threads.append(artist_thread)
            threads.append(artist_thread)
            artist_thread.start()

        for thread in threads:
            thread.join()

    def get_results(self) -> Optional[artist.Artist]:
        found_artist: Optional[artist.Artist] = None
        for artist_provider_thread in self.artist_provider_threads:
            if artist_provider_thread.result is not None:
                if found_artist is None:
                    found_artist = artist_provider_thread.result
                else:
                    found_artist.merge(artist_provider_thread.result)

        return found_artist


class AbstractArtistThread(Thread):
    def __init__(self, artist_provider: AbstractArtistProvider) -> None:
        Thread.__init__(self)
        self.artist_provider: AbstractArtistProvider = artist_provider
        self.artist_provider_ids: ObjectIds = artist_provider.get_object_ids()
        self.result: Any[Optional[artist.Artist], str]


class ArtistProviderThread(AbstractArtistThread):
    def run(self):
        self.result = self.artist_provider.get_artist()


class ArtistInformationThread(AbstractArtistThread):
    def run(self):
        self.result = self.artist_provider.get_information()


class ArtistNewsThread(AbstractArtistThread):
    def run(self):
        self.result = self.artist_provider.get_news()
