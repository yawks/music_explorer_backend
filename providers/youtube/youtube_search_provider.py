from typing import List, Tuple
from ytmusicapi import YTMusic
from providers.youtube.youtube_id import YoutubeId
from providers.youtube.youtube_utils import convert_duration
from providers.youtube.youtube_provider_information import YoutubeProviderInformation
from providers.abstract_search_provider import AbstractSearchProvider
from providers.entities.genre import Genre
from providers.entities.album import Album
from providers.entities.artist import Artist
from providers.entities.track import Track
from providers.entities.playlist import Playlist


class YoutubeSearchProvider(AbstractSearchProvider, YoutubeProviderInformation):

    def __init__(self) -> None:
        super().__init__()
        self.ytmusic = YTMusic()

    def search(self, query: str) -> Tuple[List[Track], List[Artist], List[Album], List[Genre], List[Playlist]]:
        tracks: List[Track] = self.search_track(query)
        artists: List[Artist] = []
        albums: List[Album] = []
        genres: List[Genre] = []
        playlists: List[Playlist] = self.search_playlist(query)

        return (tracks, artists, albums, genres, playlists)

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

    def search_track(self, query: str) -> List[Track]:
        tracks: List[Track] = []
        for track_dict in self.ytmusic.search(query, filter="songs"):
            track: Track = Track(
                track_id=YoutubeId(track_dict["videoId"]),
                title=track_dict["title"],
                artist=Artist(
                    artist_id=YoutubeId(track_dict["artists"][0]["id"]),
                    name=track_dict["artists"][0]["name"]),
                duration=convert_duration(track_dict["duration"]),
                external_url="https://youtube.com/watch?v=" + track_dict["videoId"],
            )
            for thumbnail in track_dict["thumbnails"]:
                track.pictures_url.append(thumbnail["url"])
            tracks.append(track)

        return tracks
