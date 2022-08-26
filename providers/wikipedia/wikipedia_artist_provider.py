from providers.entities import artist
from providers.entities.artist_news import ArtistNews
from wikipedia.exceptions import PageError
from providers.entities.album import Album
from providers.entities.object_ids import ObjectIds
from providers.entities.song import Song
from providers.entities.artist import Artist
from typing import List, Optional
from providers.abstract_artist_provider import AbstractArtistProvider
import wikipedia
from providers.wikipedia.wikipedia_id import WikipediaId


class WikipediaArtistProvider(AbstractArtistProvider):

    def __init__(self, artist_object_ids: ObjectIds, language: str = "en") -> None:
        super().__init__(artist_object_ids)
        wikipedia.set_lang(language)

    def get_object_ids(self) -> ObjectIds:
        return self.artist_object_ids

    def get_information(self) -> Optional[str]:
        information: Optional[str] = None
        try:
            page = wikipedia.page(self.artist_object_ids.obj_query_name)
            information = page.content
        except PageError:
            # TODO search instead?
            pass

        return information

    def get_all_albums(self) -> Optional[List[Album]]:
        return None

    def get_similar_artists(self) -> Optional[List[Artist]]:
        return None

    def get_top_albums(self) -> Optional[List[Album]]:
        return None

    def get_top_songs(self) -> Optional[List[Song]]:
        return None

    def get_news(self) -> Optional[List[ArtistNews]]:
        return None

    def get_artist(self) -> Optional[Artist]:
        artist: Optional[Artist] = None
        if self.artist_object_ids.obj_query_name != "":
            artist = Artist(WikipediaId(
                self.artist_object_ids.obj_query_name), self.artist_object_ids.obj_query_name)

            page = wikipedia.page(self.artist_object_ids.obj_query_name)

            for image in page.images:
                artist.pictures_url.append(image)

        return artist
