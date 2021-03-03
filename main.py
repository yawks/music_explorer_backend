#!/usr/bin/env python3
from utils.config import Config
from server.music_explorer_http_server import MusicExplorerHTTPServer
from server.http_request_handler import HTTPRequestHandler
import logging
import os
import sys


def main(argv):

    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
    httpd = MusicExplorerHTTPServer((Config.instance().get(
        "server", "host", default_value="127.0.0.1"), Config.instance().get("server", "port", default_value=8080)), HTTPRequestHandler)

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
