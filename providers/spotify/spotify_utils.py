from providers.spotify.spotify_id import SpotifyId
from providers.entities.object_id import ObjectId
from providers.entities.track import Track
from providers.entities.artist import Artist
from providers.entities.playlist import Playlist
from typing import List, cast
from providers.entities.album import Album


def get_albums(albums: dict) -> List[Album]:
    results: List[Album] = []

    if "items" in albums:
        for item in albums["items"]:
            album: Album = Album(
                album_id=SpotifyId(item["id"]),
                name=item["name"], artist=Artist(
                    artist_id=SpotifyId(item["artists"][0]["id"]),
                    name=item["artists"][0]["name"]))
            for image in item["images"]:
                album.pictures_url.append(image["url"])
            results.append(album)

    return results


def get_artists(artists: dict) -> List[Artist]:
    results: List[Artist] = []

    items: List[dict] = []
    if "items" in artists:
        items = artists["items"]
    elif "artists" in artists:
        items = artists["artists"]

    for item in items:
        artist: Artist = Artist(SpotifyId(item["id"]), item["name"])
        for image in item["images"]:
            artist.pictures_url.append(image["url"])

        results.append(artist)

    return results


def get_tracks(tracks: dict) -> List[Track]:
    results: List[Track] = []

    if "items" in tracks:
        for item in tracks["items"]:
            results.append(get_track(item))
    elif "tracks" in tracks:
        for item in tracks["tracks"]:
            results.append(get_track(item))

    return results


def get_track(item_track: dict) -> Track:
    item: dict = item_track
    if "track" in item_track:
        item = item_track["track"]

    return Track(track_id=SpotifyId(item["uri"]),
                title=item["name"],
                artist=Artist(
                    SpotifyId(item["artists"][0]["id"]), item["artists"][0]["name"]),
                duration=int(item["duration_ms"]/1000),
                stream_url=item["preview_url"])


def get_playlists(playlists: dict) -> List[Playlist]:
    results: List[Playlist] = []

    if "items" in playlists:
        for item in playlists["items"]:
            playlist: Playlist = Playlist(
                name=item["name"], playlist_id=SpotifyId(item["id"]))
            if "images" in item and len(item["images"]) > 0:
                playlist.pictures_url.append(item["images"][0]["url"])

            results.append(playlist)

    return results
