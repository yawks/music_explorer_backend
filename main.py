#!/usr/bin/env python3
from flask import Flask
from flask_restx import Resource, Api
from providers.objectid_manager import ObjectIdManager
from server.album.album_handler import AlbumHandler
from server.artist.artist_handler import ArtistHandler, ArtistQueryType
from server.search.search_handler import SearchHandler
from server.song.song_handler import SongHandler

app = Flask(__name__)
api = Api(app)


@api.route('/search/<string:search>')
class SearchMusic(Resource):
    def get(self, search: str):
        return SearchHandler(search).get_results()


@api.route('/get_album/<string:album_id>')
class GelAlbum(Resource):
    def get(self, album_id: str):
        return AlbumHandler(
            ObjectIdManager().loads(album_id)).get_results()


@api.route('/get_artist/<string:artist_id>')
class GelArtist(Resource):
    def get(self, artist_id: str):
        return ArtistHandler(
            ObjectIdManager().loads(artist_id), ArtistQueryType.ARTIST).get_results()


@api.route('/get_song/<string:song_id>')
class GelSong(Resource):
    def get(self, song_id: str):
        return SongHandler(
            ObjectIdManager().loads(song_id)).get_results()


if __name__ == '__main__':
    app.run(debug=True)
