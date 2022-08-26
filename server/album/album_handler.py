from providers.entities.object_ids import ObjectIds
from providers.entities import album
from providers.abstract_album_provider import AbstractAlbumProvider
from threading import Thread
from providers.providers_manager import ProviderManager
from typing import List, Optional


class AlbumHandler():

    def __init__(self, album_ids: ObjectIds) -> None:
        self.album_ids: ObjectIds = album_ids
        self.album_provider_threads: List[AlbumProviderThread] = []
        threads: list = []
        try:
            for album_provider_class in ProviderManager.instance().get_album_providers():
                album_provider_thread: AlbumProviderThread = AlbumProviderThread(
                    album_provider_class(), album_ids)
                self.album_provider_threads.append(album_provider_thread)
                threads.append(album_provider_thread)
                album_provider_thread.start()

            for thread in threads:
                thread.join()
        except Exception as e:
            print(str(e))

    def get_results(self) -> Optional[album.Album]:
        found_album: Optional[album.Album] = None
        for album_provider_thread in self.album_provider_threads:
            if album_provider_thread.album is not None:
                if found_album is None:
                    found_album = album_provider_thread.album
                else:
                    found_album.merge(album_provider_thread.album)

        return found_album


class AlbumProviderThread(Thread):
    def __init__(self, album_provider: AbstractAlbumProvider, album_provider_ids: ObjectIds) -> None:
        Thread.__init__(self)
        self.album_provider: AbstractAlbumProvider = album_provider
        self.album_provider_ids: ObjectIds = album_provider_ids
        self.album: Optional[album.Album]

    def run(self):
        self.album = self.album_provider.get_album(self.album_provider_ids)
