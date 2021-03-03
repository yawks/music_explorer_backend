from typing import List
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.song import Song
from providers.entities.playlist import Playlist


class SearchResult():

    def __init__(self, songs: List[Song], artists: List[Artist], albums: List[Album], genres: List[Genre], playlists: List[Playlist]) -> None:
        self.songs: List[Song] = songs
        self.artists: List[Artist] = artists
        self.albums: List[Album] = albums
        self.genres: List[Genre] = genres
        self.playlists: List[Playlist] = playlists
