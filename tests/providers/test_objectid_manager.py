from providers.spotify.spotify_id import SpotifyId
from providers.youtube.youtube_id import YoutubeId
from providers.objectid_manager import ObjectIdManager
from providers.entities.object_ids import ObjectIds


def test_dumps():
    assert ObjectIdManager().dumps(SpotifyId(
        "1235")) == "eyJzcCI6ICIxMjM1In0="


def test_dumps_list():
    object_ids:ObjectIds = ObjectIds(SpotifyId("1234"))
    object_ids.add_provider_object_id(YoutubeId("ABCD"))
    assert ObjectIdManager().dumps_list(object_ids) == "eyJzcCI6ICIxMjM0IiwgInl0IjogIkFCQ0QifQ=="


def test_loads():
    object_ids: ObjectIds = ObjectIdManager().loads(
        "eyJzcCI6ICIxMjM0IiwgInl0IjogIkFCQ0QifQ==")
    assert len(object_ids.object_id_dict) == 2
