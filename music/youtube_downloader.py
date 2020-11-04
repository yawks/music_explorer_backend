import json
import pafy
import os
from datetime import datetime

DOWNLOAD_DIRECTORY = "download"


class YoutubeDownloader():
    def __init__(self, youtube_id: str) -> None:
        # first find if the audio has already been downloaded
        self.music_information_file: str = "%s/%s.txt" % (
            DOWNLOAD_DIRECTORY, youtube_id)
        if os.path.isfile(self.music_information_file):
            with open(self.music_information_file) as json_file:
                js = json.load(json_file)
                self.filename = js["filename"]
                self.content_type = js["content_type"]
        else:
            p = pafy.new(youtube_id)
            ba = p.getbestaudio()
            self.filename = ba.filename
            ba.download(filepath="%s/%s" %
                        (DOWNLOAD_DIRECTORY, self.filename), quiet=True)
            self.content_type = "%s/%s" % (ba.mediatype, ba.extension)

        self._write_music_information_file()

    def get_filename(self):
        return "%s/%s" % (DOWNLOAD_DIRECTORY, self.filename)

    def get_content_type(self):
        return self.content_type

    def _write_music_information_file(self):
        with open(self.music_information_file, "w") as outfile:
            js = {
                "filename": self.filename,
                "content_type": self.content_type,
                "last_access": datetime.now().strftime("%Y-%m-%d - %H:%M:%S")
            }
            json.dump(js, outfile)
