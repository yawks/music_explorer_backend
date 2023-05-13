import json
from typing import List, Optional
from threading import Thread
from providers.entities.abstract_entity import EntityEncoder
from providers.entities.object_ids import ObjectIds
from providers.entities import song
from providers.abstract_song_provider import AbstractSongProvider
from providers.providers_manager import ProviderManager


class SongHandler():
    """Gather song providers' results
    """

    def __init__(self, song_ids: ObjectIds) -> None:
        self.song_ids: ObjectIds = song_ids
        self.song_provider_threads: List[SongProviderThread] = []
        threads: list = []
        try:
            for song_provider_class in ProviderManager().get_song_providers():
                try:
                    song_provider_thread: SongProviderThread = SongProviderThread(
                        song_provider_class(), song_ids)
                    self.song_provider_threads.append(song_provider_thread)
                    threads.append(song_provider_thread)
                    song_provider_thread.start()
                except Exception as e:
                    print(str(e))

            for thread in threads:
                thread.join()
        except Exception as e:
            print(str(e))

    def get_results(self) -> dict:
        found_song: Optional[song.Song] = None
        for song_provider_thread in self.song_provider_threads:
            if song_provider_thread.song is not None:
                if found_song is None:
                    found_song = song_provider_thread.song
                else:
                    found_song.merge(song_provider_thread.song)

        return json.loads(json.dumps(  # TODO : fix this
            found_song, cls=EntityEncoder))


class SongProviderThread(Thread):
    def __init__(self, song_provider: AbstractSongProvider, song_provider_ids: ObjectIds) -> None:
        Thread.__init__(self)
        self.song_provider: AbstractSongProvider = song_provider
        self.song_provider_ids: ObjectIds = song_provider_ids
        self.song: Optional[song.Song]

    def run(self):
        self.song = self.song_provider.get_song(self.song_provider_ids)
