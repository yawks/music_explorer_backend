from providers.abstract_artist_provider import AbstractArtistProvider
from typing import List, Optional
from utils.config import Config
from .api.api import MusicStoryApi
from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.song import Song
from providers.entities.artist import Artist
from providers.entities.album import Album


class MusicStoryArtistProvider(AbstractArtistProvider):

    def __init__(self, artist: Artist) -> None:
        self.music_story = MusicStoryApi(Config.instance().get("providers", "music_story", "consumer_key"),
                                         Config.instance().get("providers", "music_story", "consumer_secret"))
        try:
            self.music_story.connect()
            self.artist = artist
            self.artist_id: int = -1
            results = self.music_story.search("artist", name=self.artist.name)
            #s elf.artist_id = results[0].id
        except Exception as e:
            print(str(e))
            #TODO : log

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
        try:
            if self.artist_id > -1:
                results = self.music_story.get(
                    "news", id=self.artist_id, lang=Config.instance().get("lang")[0])
                a = "2"
        except Exception as e:
            print(str(e))
            #TODO : log
            
        return news
