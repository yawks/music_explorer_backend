from glob import glob
import importlib
import inspect
import os
from typing import Dict, Tuple


class ProviderManager():
    _self = None
    providers: Dict[str, dict] = {}

    def __init__(self) -> None:
        for dir in glob("providers/*"):
            if os.path.isdir(dir):
                self._load_providers(dir)

    def __new__(cls):
        if cls._self is None:
            cls._self = super().__new__(cls)
        return cls._self

    def _load_providers(self, dir: str):
        for provider_path in glob("%s/*.py" % dir):
            if provider_path.strip(dir) != "__init__.py":
                module_name, package_name = self._get_module_and_package_name(
                    provider_path)

                module = importlib.import_module(
                    module_name, package=package_name)
                self._search_for_provider_classes(provider_path, module)

    def _search_for_provider_classes(self, provider_path, module):
        for abstract_provider in ["AbstractSearchProvider", "AbstractPlaylistProvider", "AbstractAlbumProvider", "AbstractArtistProvider", "AbstractTrackProvider"]:
            if hasattr(module, abstract_provider):
                for member in inspect.getmembers(module):
                    self._load_provider_module(
                        provider_path, abstract_provider, module, member)

    def _get_module_and_package_name(self, provider_path: str) -> Tuple[str, str]:
        module_name: str = ".%s" % os.path.basename(provider_path)
        package_name: str = os.path.dirname(
            provider_path).replace(os.path.sep, ".")

        thelen = len(".py")
        if module_name[-thelen:] == ".py":
            module_name = module_name[:-thelen]

        return (module_name, package_name)

    def _load_provider_module(self, provider_path: str, abstract_provider: str, module, provider_class):
        if provider_class[0].find("__") == -1 \
                and isinstance(provider_class[1], type) \
                and issubclass(provider_class[1], getattr(module, abstract_provider, "")) \
                and provider_class[1].__name__ != abstract_provider:

            provider_name: str = provider_path.split(os.path.sep)[1]
            if provider_name not in self.providers:
                self.providers[provider_name] = dict()

            self.providers[provider_name][abstract_provider] = provider_class[1]

    def get_search_providers(self) -> list:
        return self._get_providers_implementing("AbstractSearchProvider")

    def get_album_providers(self) -> list:
        return self._get_providers_implementing("AbstractAlbumProvider")

    def get_artist_providers(self) -> list:
        return self._get_providers_implementing("AbstractArtistProvider")

    def get_playlist_providers(self) -> list:
        return self._get_providers_implementing("AbstractPlaylistProvider")

    def get_track_providers(self) -> list:
        return self._get_providers_implementing("AbstractTrackProvider")

    def _get_providers_implementing(self, abstract_provider: str) -> list:
        providers: list = []

        for provider_name in self.providers:
            for ap in self.providers[provider_name]:
                if abstract_provider == ap:
                    providers.append(
                        self.providers[provider_name][abstract_provider])

        return providers

    def list(self, provider_type: str) -> dict:
        result = {}
        if provider_type == "track":
            result = self._get_providers_implementing("AbstractTrackProvider")

        return result
