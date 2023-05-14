from typing import List, Optional
import wikipedia
from utils.config import Config
from wikipedia.exceptions import PageError
from providers.entities.artist_news import ArtistNews
from providers.entities.album import Album
from providers.entities.object_ids import ObjectId
from providers.entities.track import Track
from providers.entities.artist import Artist
from providers.abstract_artist_provider import AbstractArtistProvider
from providers.wikipedia.wikipedia_id import WikipediaId
from providers.wikipedia.wikipedia_provider_information import WikipediaProviderInformation


class WikipediaArtistProvider(AbstractArtistProvider, WikipediaProviderInformation):

    def __init__(self, object_id: ObjectId, name: str) -> None:
        super().__init__(object_id, name)
        wikipedia.set_lang(Config().get_languages()[0])

    def get_information(self) -> Optional[str]:
        information: Optional[str] = None
        if self.name != "":
            try:
                page = wikipedia.page(self.name)
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

    def get_top_tracks(self) -> Optional[List[Track]]:
        return None

    def get_news(self) -> Optional[List[ArtistNews]]:
        return None

    def get_artist(self) -> Optional[Artist]:
        artist: Optional[Artist] = None
        if self.name != "":
            artist = Artist(WikipediaId(self.name), self.name)

            page = wikipedia.page(self.name)

            for image in page.images:
                artist.pictures_url.append(image)

        return artist
