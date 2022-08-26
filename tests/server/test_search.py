from server.search.search_result import SearchResult
from typing import List
from server.search.search_handler import SearchHandler


def test_search():
    search: SearchHandler = SearchHandler("led zeppelin")

    result: SearchResult = search.get_results()

    if len(result.songs) == 0:
        raise AssertionError("result must not be empty")
