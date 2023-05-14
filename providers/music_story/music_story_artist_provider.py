from typing import List, Optional
from utils.config import Config
from providers.entities.object_ids import ObjectId
from providers.abstract_artist_provider import AbstractArtistProvider
from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.track import Track
from providers.entities.artist import Artist
from providers.music_story.music_story_provider_information import MusicStoryProviderInformation
from .api.api import MusicStoryApi

class MusicStoryArtistProvider(AbstractArtistProvider, MusicStoryProviderInformation):

    def __init__(self, object_id: ObjectId, name: str) -> None:
        super().__init__(object_id, name)
        self.music_story = MusicStoryApi(Config().get("providers", "music_story", "consumer_key"),
                                         Config().get("providers", "music_story", "consumer_secret"))

    def get_information(self) -> Optional[str]:
        return None

    def get_top_tracks(self) -> Optional[List[Track]]:
        return None

    def get_top_albums(self) -> Optional[List[Album]]:
        return None

    def get_all_albums(self) -> Optional[List[Album]]:
        return None

    def get_similar_artists(self) -> Optional[List[Artist]]:
        return None

    def get_news(self) -> Optional[List[ArtistNews]]:
        news: Optional[List[ArtistNews]] = []
        
        try:
            result = self.music_story.get(
                "news", id=self.object_id, lang=Config().get_languages()[0])
            #MusicStoryObject
        except Exception as e:
            print(str(e))
            #TODO : log
        
        return news

    def get_artist(self) -> Optional[Album]:
        try:
            self.music_story.connect()
            _ = self.music_story.get(
                "news", id=self.object_id, lang=Config().get_languages()[0])

            """
            _ = s elf.music_story.search(
                "artist", name=self.artist_object_ids.obj_query_name)
            # s elf.artist_id = results[0].id
        """

        except Exception as e:
            print(str(e))
            #TODO : log
        return None
