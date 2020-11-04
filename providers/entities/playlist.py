from typing import List, Optional


class Playlist():
    name: str
    playlist_id: Optional[str]
    pictures_url: List[str]

    def __init__(self, name: str, playlist_id: Optional[str] = None) -> None:
        self.name = name
        self.playlist_id = playlist_id
        self.pictures_url = []
