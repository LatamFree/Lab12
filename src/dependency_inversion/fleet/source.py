from abc import ABC, abstractclassmethod

class Source(ABC):
    @abstractclassmethod
    def get_data(self):
        pass