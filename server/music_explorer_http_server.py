from http.server import HTTPServer

LISTENING_HOSTNAME = "192.168.1.71"
LISTENING_PORT = 8080

class MusicExplorerHTTPServer(HTTPServer):

    def get_protocol(self) -> str:
        protocol = "http"
        
        return protocol

    def get_listening_url_prefix(self):
        return "%s://%s:%d" % (
            self.get_protocol(),
            LISTENING_HOSTNAME,
            LISTENING_PORT)
