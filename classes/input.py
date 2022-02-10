from abc import ABC, abstractmethod


class Input(ABC):

    @abstractmethod
    def append(self, output):
        pass
