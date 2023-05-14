from providers.abstract_provider_information import AbstractProviderInformation


class SpotifyProviderInformation(AbstractProviderInformation):

    def __init__(self) -> None:
        super().__init__(name="Spotify", icon="spotify.png")
