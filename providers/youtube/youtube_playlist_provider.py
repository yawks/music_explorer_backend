from providers.youtube.youtube_id import YoutubeId
from providers.youtube.youtube_utils import convert_duration
from providers.entities.artist import Artist
from providers.entities.playlist import Playlist
from providers.abstract_playlist_provider import AbstractPlaylistProvider
from providers.entities.song import Song
from typing import List, Optional
from ytmusicapi import YTMusic


class YoutubePlaylistProvider(AbstractPlaylistProvider):

    def __init__(self, playlist: Playlist) -> None:
        self.playlist: Playlist = playlist
        self.ytmusic = YTMusic()

    def get_songs(self) -> List[Song]:
        songs: List[Song] = []
        playlist_id: Optional[str] = self.playlist.get_object_ids().get_id(
            YoutubeId.get_short_name())
        if playlist_id is not None:
            result: dict = self.ytmusic.get_playlist(playlist_id)
            for track in result["tracks"]:
                song: Song = Song(
                    song_id=YoutubeId(track["videoId"]),
                    title=track["title"], artist=Artist(
                        artist_id=track["artists"][0]["id"],
                        name=track["artists"][0]["name"]),
                    duration=convert_duration(track["duration"]),
                    stream_url=track["videoId"])
                for thumbnail in track["thumbnails"]:
                    song.pictures_url.append(thumbnail["url"])

                songs.append(song)

        return songs
