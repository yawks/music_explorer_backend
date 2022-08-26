from providers.entities.object_ids import ObjectIds
from providers.abstract_artist_provider import AbstractArtistProvider
from typing import List, Optional
from utils.config import Config
from .api.api import MusicStoryApi
from .music_story_id import MusicStoryId
from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.song import Song
from providers.entities.artist import Artist
from providers.entities.album import Album


class MusicStoryArtistProvider(AbstractArtistProvider):

    def __init__(self, artist_object_ids: ObjectIds) -> None:
        super().__init__(artist_object_ids)
        self.music_story = MusicStoryApi(Config.instance().get("providers", "music_story", "consumer_key"),
                                         Config.instance().get("providers", "music_story", "consumer_secret"))

    def get_object_ids(self) -> ObjectIds:
        return self.artist_object_ids

    def get_information(self) -> Optional[str]:
        return None

    def get_top_songs(self) -> Optional[List[Song]]:
        return None

    def get_top_albums(self) -> Optional[List[Album]]:
        return None

    def get_all_albums(self) -> Optional[List[Album]]:
        return None

    def get_similar_artists(self) -> Optional[List[Artist]]:
        return None

    def get_news(self) -> Optional[List[ArtistNews]]:
        news: Optional[List[ArtistNews]] = None
        """

        t ry:
            if self.artist_id > -1:
                _ = self.music_story.get(
                    "news", id=self.artist_id, lang=Config.instance().get("lang")[0])
                # a a = "2"
        except Exception as e:
            print(str(e))
            #TODO : log
        """

        return news

    def get_artist(self) -> Optional[Album]:
        try:
            self.music_story.connect()
            _ = self.music_story.get(
                "news", id=self.artist_object_ids.get_id(MusicStoryId), lang=Config.instance().get("lang")[0])

            """
            _ = s elf.music_story.search(
                "artist", name=self.artist_object_ids.obj_query_name)
            # s elf.artist_id = results[0].id
        """

        except Exception as e:
            print(str(e))
            #TODO : log
        return None
