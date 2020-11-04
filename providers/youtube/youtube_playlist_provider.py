from providers.youtube.youtube_utils import convert_duration
from providers.entities.artist import Artist
from providers.entities.playlist import Playlist
from providers.abstract_playlist_provider import AbstractPlaylistProvider
from providers.entities.song import Song
from typing import List
from ytmusicapi import YTMusic


class YoutubePlaylistProvider(AbstractPlaylistProvider):

    def __init__(self, playlist: Playlist) -> None:
        self.playlist: Playlist = playlist
        self.ytmusic = YTMusic()

    def get_songs(self) -> List[Song]:
        songs: List[Song] = []
        if self.playlist.playlist_id is not None:
            result: dict = self.ytmusic.get_playlist(self.playlist.playlist_id)
            for track in result["tracks"]:
                song: Song = Song(title=track["title"], artist=Artist(
                    track["artists"][0]["name"]),
                    duration=convert_duration(track["duration"]),
                    stream_url=track["videoId"])
                for thumbnail in track["thumbnails"]:
                    song.pictures_url.append(thumbnail["url"])
                
                songs.append(song)

        return songs
