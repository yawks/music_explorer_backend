from typing import List, Tuple, cast
from threading import Thread
from server.search.search_result import SearchResult
from providers.entities.abstract_entity import AbstractEntity
from providers.providers_manager import ProviderManager
from providers.abstract_search_provider import AbstractSearchProvider
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.entities.playlist import Playlist


class SearchHandler():

    def __init__(self, query: str) -> None:
        self.query: str = query
        self.search_provider_threads: List[SearchProviderThread] = []
        threads: list = []
        for search_provider_class in ProviderManager().get_search_providers():
            try:
                search_provider_thread: SearchProviderThread = SearchProviderThread(
                    search_provider_class(), query)
                self.search_provider_threads.append(search_provider_thread)
                threads.append(search_provider_thread)
                search_provider_thread.start()

            except Exception as e:
                print(str(e))

        for thread in threads:
            thread.join()

    def get_results(self) -> dict:
        tracks: List[Track] = []
        artists: List[Artist] = []
        albums: List[Album] = []
        genres: List[Genre] = []
        playlists: List[Playlist] = []

        for search_provider_thread in self.search_provider_threads:
            results: Tuple[List[Track], List[Artist],
                           List[Album], List[Genre], List[Playlist]] = search_provider_thread.results
            tracks = cast(List[Track], self._merge_entities(
                cast(List[AbstractEntity], tracks), cast(List[AbstractEntity], results[0])))

            artists = cast(List[Artist], self._merge_entities(
                cast(List[AbstractEntity], artists), cast(List[AbstractEntity], results[1])))

            albums = cast(List[Album], self._merge_entities(
                cast(List[AbstractEntity], albums), cast(List[AbstractEntity], results[2])))

            genres = cast(List[Genre], self._merge_entities(
                cast(List[AbstractEntity], artists), cast(List[AbstractEntity], results[3])))

            playlists = cast(List[Playlist], self._merge_entities(
                cast(List[AbstractEntity], artists), cast(List[AbstractEntity], results[4])))

        return SearchResult(tracks, artists, albums, genres, playlists).get_json()

    def _merge_entities(self, a_entities: List[AbstractEntity], b_entities: List[AbstractEntity]) -> List[AbstractEntity]:
        merged_entities: List[AbstractEntity] = b_entities

        for other_entity in a_entities:
            found: bool = False
            for entity in b_entities:
                if other_entity == entity:
                    entity.merge(other_entity)
                    found = True
                    break

            if not found:
                merged_entities.append(other_entity)

        return merged_entities


class SearchProviderThread(Thread):
    def __init__(self, search_provider: AbstractSearchProvider, query: str) -> None:
        Thread.__init__(self)
        self.search_provider: AbstractSearchProvider = search_provider
        self.query: str = query
        self.results: Tuple[List[Track], List[Artist],
                            List[Album], List[Genre], List[Playlist]] = ([], [], [], [], [])

    def run(self):
        self.results = self.search_provider.search(self.query)
