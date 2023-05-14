from providers.youtube.youtube_id import YoutubeId
from providers.youtube.youtube_utils import convert_duration
from providers.entities.artist import Artist
from providers.entities.playlist import Playlist
from providers.abstract_playlist_provider import AbstractPlaylistProvider
from providers.entities.track import Track
from typing import List, Optional
from ytmusicapi import YTMusic


class YoutubePlaylistProvider(AbstractPlaylistProvider):

    def __init__(self, playlist: Playlist) -> None:
        self.playlist: Playlist = playlist
        self.ytmusic = YTMusic()

    def get_tracks(self) -> List[Track]:
        tracks: List[Track] = []
        playlist_id: Optional[str] = self.playlist.get_object_ids().get_id(
            YoutubeId.get_short_name())
        if playlist_id is not None:
            result: dict = self.ytmusic.get_playlist(playlist_id)
            for track_dict in result["tracks"]:
                track: Track = Track(
                    track_id=YoutubeId(track_dict["videoId"]),
                    title=track_dict["title"], artist=Artist(
                        artist_id=track_dict["artists"][0]["id"],
                        name=track_dict["artists"][0]["name"]),
                    duration=convert_duration(track_dict["duration"]),
                    stream_url=track_dict["videoId"])
                for thumbnail in track_dict["thumbnails"]:
                    track.pictures_url.append(thumbnail["url"])

                tracks.append(track)

        return tracks
