from providers.entities.object_ids import ObjectIds
from providers.objectid_manager import ObjectIdManager, object_id_serializer
from typing import Dict
import jsons
from urllib.parse import unquote
from music.youtube_downloader import YoutubeDownloader
from server.search.search import Search
from server.album.album import Album
from http.server import BaseHTTPRequestHandler

HEADER_CONTENT_TYPE_KEY = "Content-type"
HEADER_CONTENT_TYPE_VALUE = "application/json"
ACCESS_CONTROL_ALLOW_ORIGIN_KEY = "Access-Control-Allow-Origin"
ACCESS_CONTROL_ALLOW_ORIGIN_VALUE = "*"


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        handler_by_prefix: dict = {
            "/search/": self._search,
            "/song/": self._song,
            "/album/": self._album,
            "/youtube_get/": self._youtube_get
        }

        fn = self._home
        query: str = ""
        for prefix in handler_by_prefix:
            if self.path.startswith(prefix):
                fn = handler_by_prefix[prefix]
                query = self.path[len(prefix):].strip()
                break
        fn(query)

    def _search(self, query: str):
        self._set_headers(
            200, {HEADER_CONTENT_TYPE_KEY: HEADER_CONTENT_TYPE_VALUE,
                  ACCESS_CONTROL_ALLOW_ORIGIN_KEY: ACCESS_CONTROL_ALLOW_ORIGIN_VALUE})

        self.respond(jsons.dumps(
            Search(query).get_results(), default=vars))

    def _youtube_get(self, youtube_id: str):
        if len(youtube_id) > 0:
            youtube_downloader: YoutubeDownloader = YoutubeDownloader(
                youtube_id)
            self._set_headers(
                200, {
                    HEADER_CONTENT_TYPE_KEY: youtube_downloader.get_content_type(),
                    "Content-Disposition": "attachment; filename=\"%s\"" % youtube_downloader.filename})

            f = open(youtube_downloader.get_filename(), "rb")
            self.wfile.write(f.read())
            f.close()

    def _song(self, query: str):
        self._set_headers(
            200, {HEADER_CONTENT_TYPE_KEY: HEADER_CONTENT_TYPE_VALUE,
                  ACCESS_CONTROL_ALLOW_ORIGIN_KEY: ACCESS_CONTROL_ALLOW_ORIGIN_VALUE})

    def _album(self, album_id: str):
        self._set_headers(
            200, {HEADER_CONTENT_TYPE_KEY: HEADER_CONTENT_TYPE_VALUE,
                  ACCESS_CONTROL_ALLOW_ORIGIN_KEY: ACCESS_CONTROL_ALLOW_ORIGIN_VALUE})
        self.respond(jsons.dumps(
            Album(ObjectIdManager.instance().loads(album_id)).get_results()))

    def _home(self, query: str):
        self._set_headers(
            200, {HEADER_CONTENT_TYPE_KEY: HEADER_CONTENT_TYPE_VALUE,
                  ACCESS_CONTROL_ALLOW_ORIGIN_KEY: ACCESS_CONTROL_ALLOW_ORIGIN_VALUE})
        self.respond('''{"items": [{
            "name": "Rock",
            "picture": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e0fc4bb1-7582-4557-9386-046b61787bb3/d2lk6ow-08564a5a-d3ce-4b98-a8b5-7f0445092e73.jpg/v1/fill/w_894,h_894,q_70,strp/generic_rock_album_cover_by_justmardesign_d2lk6ow-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3siaGVpZ2h0IjoiPD0xNDI1IiwicGF0aCI6IlwvZlwvZTBmYzRiYjEtNzU4Mi00NTU3LTkzODYtMDQ2YjYxNzg3YmIzXC9kMmxrNm93LTA4NTY0YTVhLWQzY2UtNGI5OC1hOGI1LTdmMDQ0NTA5MmU3My5qcGciLCJ3aWR0aCI6Ijw9MTQyNSJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.9l9Oqr6uzyp1au9m3FCHSud5Vo4BpbRVxlrQhPZFY4o"
        },
        {
            "name": "Rap1",
            "picture": "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/rap-hip-hop-cover-world-through-a-diamond-design-template-006e571932e5611386b331c8c4a3862f_screen.jpg?ts=1581497345"
        },
        {
            "name": "Rap2",
            "picture": "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/rap-hip-hop-cover-world-through-a-diamond-design-template-006e571932e5611386b331c8c4a3862f_screen.jpg?ts=1581497345"
        },
        {
            "name": "Rap3",
            "picture": "https://d1csarkz8obe9u.cloudfront.net/posterpreviews/rap-hip-hop-cover-world-through-a-diamond-design-template-006e571932e5611386b331c8c4a3862f_screen.jpg?ts=1581497345"
        }]}''')

    def respond(self, content: str):
        self.wfile.write(bytes(content, 'UTF-8'))

    def _set_headers(self, code: int, headers: Dict[str, str]):
        self.send_response(code)
        for header, value in headers.items():
            self.send_header(header, value)
        self.end_headers()
        jsons.set_serializer(object_id_serializer, ObjectIds)
