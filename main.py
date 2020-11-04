#!/usr/bin/env python3
from server.music_explorer_http_server import MusicExplorerHTTPServer, LISTENING_PORT, LISTENING_HOSTNAME
from server.http_request_handler import HTTPRequestHandler
import logging
import os
import sys


def main(argv):

    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    httpd = MusicExplorerHTTPServer((LISTENING_HOSTNAME, LISTENING_PORT), HTTPRequestHandler)

    logging.getLogger().info("Server Starts - %s",
                             httpd.get_listening_url_prefix())
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.getLogger().info("Server Stops")


if __name__ == "__main__":
    main(sys.argv)
