from providers.abstract_provider_information import AbstractProviderInformation


class MusicBrainzProviderInformation(AbstractProviderInformation):

    def __init__(self) -> None:
        super().__init__(name="Music Brainz", icon="musicbrainz.png")
