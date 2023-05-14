from providers.abstract_provider_information import AbstractProviderInformation


class MusicStoryProviderInformation(AbstractProviderInformation):

    def __init__(self) -> None:
        super().__init__(name="Music Story", icon="musicstory.png")
