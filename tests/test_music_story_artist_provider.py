from providers.music_story.music_story_id import MusicStoryId
from providers.entities.artist import Artist
from providers.music_story.music_story_artist_provider import MusicStoryArtistProvider

TEST_ARTIST_NAME = "led zeppelin"


def test_get_news():
    music_story_artist_provider: MusicStoryArtistProvider = MusicStoryArtistProvider(
        artist=Artist(
            artist_id=MusicStoryId("dummy"),
            name=TEST_ARTIST_NAME))

    news = music_story_artist_provider.get_news()

    assert news is not None
    assert len(news) > 0
