from providers.entities.object_id import ObjectId
from typing import List


class Genre():
    object_id: ObjectId
    name: str
    description: str
    pictures_url: List[str]