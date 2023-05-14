from providers.abstract_provider_information import AbstractProviderInformation

class YoutubeProviderInformation(AbstractProviderInformation):

    def __init__(self) -> None:
        super().__init__(name="Youtube", icon="youtube.png")
