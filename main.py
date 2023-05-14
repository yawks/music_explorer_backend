#!/usr/bin/env python3
from flask import Flask
from flask_restx import Resource, Api, Namespace
from providers.objectid_manager import ObjectIdManager
from server.album.album_handler import AlbumHandler
from server.artist.artist_handler import ArtistHandler, ArtistQueryType
from server.search.search_handler import SearchHandler
from server.track.track_handler import TrackHandler
from providers.providers_manager import ProviderManager


app = Flask(__name__)
music_api = Namespace("music", description="Music explorer")
providers_api = Namespace("providers", description="Providers informations")

api = Api(
    title="Music explorer API",
    version="1.0",
    description="Multi source music explorer API",
)
api.init_app(app)

api.add_namespace(music_api)
api.add_namespace(providers_api)

@music_api.route('/search/<string:search>')
@music_api.param("search", "search query: artist name, track title, playlist name, or album name")
class SearchMusic(Resource):
    def get(self, search: str):
        return SearchHandler(search).get_results()


@music_api.route('/get_album/<string:album_id>')
class GelAlbum(Resource):
    def get(self, album_id: str):
        return AlbumHandler(
            ObjectIdManager().loads(album_id)).get_results()


@music_api.route('/get_artist/<string:artist_id>')
class GelArtist(Resource):
    def get(self, artist_id: str):
        return ArtistHandler(
            ObjectIdManager().loads(artist_id), ArtistQueryType.ARTIST).get_results()


@music_api.route('/get_track/<string:track_id>')
class GelTrack(Resource):
    def get(self, track_id: str):
        return TrackHandler(
            ObjectIdManager().loads(track_id)).get_results()


@providers_api.route("/list/<string:provider_type>")
@providers_api.param("provider_type", "track, album, artist, playlist, search")
class GetProviders(Resource):
    def get(self, provider_type: str):
        return ProviderManager().list(provider_type)
            

if __name__ == '__main__':
    app.run(debug=True)
