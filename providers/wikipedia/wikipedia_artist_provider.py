from providers.entities.artist_news import ArtistNews
from wikipedia.exceptions import PageError
from providers.entities.album import Album
from providers.entities.song import Song
from providers.entities.artist import Artist
from typing import List, Optional
from providers.abstract_artist_provider import AbstractArtistProvider
import wikipedia


class WikipediaArtistProvider(AbstractArtistProvider):

    def __init__(self, artist: Artist, language: str = "en") -> None:
        self.artist = artist
        wikipedia.set_lang(language)

    def get_information(self) -> Optional[str]:
        information: Optional[str] = None
        try:
            page = wikipedia.page(self.artist.name)
            information = page.content

            #also enrich artist with wikipedia pictures
            for image in page.images:
                if image.lower().find(".svg") == -1:
                    self.artist.pictures_url.append(image)
        except PageError:
            #TODO search instead?
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
