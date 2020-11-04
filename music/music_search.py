from youtube_search import YoutubeSearch


class MusicSearch():

    def __init__(self, prefix_url:str, query:str) -> None:
        self.query: str = query
        self.results: dict = {}
        self.results["items"] = []
        for result in YoutubeSearch(query, max_results=10).to_dict():
            self.results["items"].append({
                "title": result["title"],
                "artist": "",
                "duration": result["duration"],
                "picture": result["thumbnails"][0],
                "id": result["id"],
                "url" : "https://youtube.com%s" % result["url_suffix"],
                "mp3_stream" : "%s/youtube_get/%s" % (prefix_url, result["id"])
            })
    

    def get_results(self) -> dict:
        return self.results