from http.server import HTTPServer
from utils.config import Config


class MusicExplorerHTTPServer(HTTPServer):

    def get_protocol(self) -> str:
        protocol = "http"

        return protocol

    def get_listening_url_prefix(self):
        return "%s://%s:%d" % (
            self.get_protocol(),
            Config.instance().get("server", "host", default_value="127.0.0.1"),
            Config.instance().get("server", "port", default_value=8080))
