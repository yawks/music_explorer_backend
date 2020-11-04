from typing import cast
from server.music_explorer_http_server import MusicExplorerHTTPServer
from music.youtube_downloader import YoutubeDownloader
from music.music_search import MusicSearch
from http.server import BaseHTTPRequestHandler
import json


class HTTPRequestHandler(BaseHTTPRequestHandler):

    def do_HEAD(self):
        return

    def do_POST(self):
        return

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin ", "*")
        self.end_headers()

        if self.path.startswith("/search/"):
            self._search()
        elif self.path.startswith("/youtube_get/"):
            self._youtube_get()
        else:
            self._home()

    def _search(self):
        self.respond(json.dumps(MusicSearch("%s://%s" % (cast(MusicExplorerHTTPServer, self.server).get_protocol(), self.headers.get('Host')),
                                            self.path[len("/search/"):]).get_results()))

    def _youtube_get(self):
        youtube_id: str = ""
        youtube_id = self.path[len("/youtube_get/"):].strip()
        if len(youtube_id) > 0:
            youtube_downloader: YoutubeDownloader = YoutubeDownloader(
                youtube_id)

            self.send_header(
                "Content-type", youtube_downloader.get_content_type())  # "audio/webm")
            f = open(youtube_downloader.get_filename(), "rb")
            self.wfile.write(f.read())
            f.close()

    def _home(self):
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
