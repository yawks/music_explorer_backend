from providers.abstract_provider_information import AbstractProviderInformation

class WikipediaProviderInformation(AbstractProviderInformation):

    def __init__(self) -> None:
        super().__init__(name="Wikipedia", icon="wikipedia.png")
