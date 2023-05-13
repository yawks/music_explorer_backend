from providers.youtube.youtube_id import YoutubeId
from providers.youtube.youtube_utils import convert_duration
from providers.abstract_search_provider import AbstractSearchProvider
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.song import Song
from providers.entities.playlist import Playlist
from typing import List, Tuple
from ytmusicapi import YTMusic
from datetime import datetime


class YoutubeSearchProvider(AbstractSearchProvider):

    def __init__(self) -> None:
        self.ytmusic = YTMusic()

    def search(self, query: str) -> Tuple[List[Song], List[Artist], List[Album], List[Genre], List[Playlist]]:
        songs: List[Song] = self.search_song(query)
        artists: List[Artist] = []
        albums: List[Album] = []
        genres: List[Genre] = []
        playlists: List[Playlist] = self.search_playlist(query)

        return (songs, artists, albums, genres, playlists)

    def search_album(self, query: str) -> List[Album]:

        return []

    def search_artist(self, query: str) -> List[Artist]:
        return []

    def search_genre(self, query: str) -> List[Genre]:
        return []

    def search_playlist(self, query: str) -> List[Playlist]:
        playlists: List[Playlist] = []
        for playlist in self.ytmusic.search(query, filter="playlists"):
            p: Playlist = Playlist(
                playlist_id=YoutubeId(playlist["browseId"]),
                name=playlist["title"])
            for thumbnail in playlist["thumbnails"]:
                p.pictures_url.append(thumbnail)
            playlists.append(p)

        return playlists

    def search_song(self, query: str) -> List[Song]:
        songs: List[Song] = []
        for song in self.ytmusic.search(query, filter="songs"):
            s: Song = Song(
                song_id=YoutubeId(song["videoId"]),
                title=song["title"],
                artist=Artist(
                    artist_id=YoutubeId(song["artists"][0]["id"]),
                    name=song["artists"][0]["name"]),
                duration=convert_duration(song["duration"]),
                external_url="https://youtube.com/watch?v=" + song["videoId"],
            )
            for thumbnail in song["thumbnails"]:
                s.pictures_url.append(thumbnail["url"])
            songs.append(s)

        return songs
