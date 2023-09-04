from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass
class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass
class Scaner(ABC):
    @abstractmethod
    def scan(self, document):
        pass
