from music_story import api
from music_story.api import MusicStoryApi

class MusicStory():

    def __init__(self) -> None:
        api = MusicStoryApi("f1ea72b33c598fd5539babcaab0adb6d4676bc6e", "5e46fa91079b6cb00a6e2edf719a06cb758ed49f")
        api.connect()

        a =api.get("genre", 66)
        a = a


if __name__ == "__main__":
    musicStory: MusicStory = MusicStory()