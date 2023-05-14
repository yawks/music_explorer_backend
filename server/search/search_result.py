from typing import List
import json
from providers.entities.abstract_entity import EntityEncoder
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.entities.playlist import Playlist


class SearchResult():

    def __init__(self, tracks: List[Track], artists: List[Artist], albums: List[Album], genres: List[Genre], playlists: List[Playlist]) -> None:
        self.tracks: List[Track] = tracks
        self.artists: List[Artist] = artists
        self.albums: List[Album] = albums
        self.genres: List[Genre] = genres
        self.playlists: List[Playlist] = playlists


    def get_json(self) -> dict:
        return json.loads(json.dumps(  # TODO : fix this
            self, cls=EntityEncoder))