import json
from typing import List, Optional
from threading import Thread
from providers.entities.abstract_entity import EntityEncoder
from providers.entities.object_ids import ObjectIds
from providers.entities import track
from providers.abstract_track_provider import AbstractTrackProvider
from providers.providers_manager import ProviderManager


class TrackHandler():
    """Gather track providers' results
    """

    def __init__(self, track_ids: ObjectIds) -> None:
        self.track_ids: ObjectIds = track_ids
        self.track_provider_threads: List[TrackProviderThread] = []
        threads: list = []
        try:
            for track_provider_class in ProviderManager().get_track_providers():
                try:
                    track_provider_thread: TrackProviderThread = TrackProviderThread(
                        track_provider_class(), track_ids)
                    self.track_provider_threads.append(track_provider_thread)
                    threads.append(track_provider_thread)
                    track_provider_thread.start()
                except Exception as e:
                    print(str(e))

            for thread in threads:
                thread.join()
        except Exception as e:
            print(str(e))

    def get_results(self) -> dict:
        found_track: Optional[track.Track] = None
        for track_provider_thread in self.track_provider_threads:
            if track_provider_thread.track is not None:
                if found_track is None:
                    found_track = track_provider_thread.track
                else:
                    found_track.merge(track_provider_thread.track)

        return json.loads(json.dumps(  # TODO : fix this
            found_track, cls=EntityEncoder))


class TrackProviderThread(Thread):
    def __init__(self, track_provider: AbstractTrackProvider, track_provider_ids: ObjectIds) -> None:
        Thread.__init__(self)
        self.track_provider: AbstractTrackProvider = track_provider
        self.track_provider_ids: ObjectIds = track_provider_ids
        self.track: Optional[track.Track]

    def run(self):
        self.track = self.track_provider.get_track(self.track_provider_ids)
