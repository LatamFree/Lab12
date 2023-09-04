from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def calculate_area(self):
        pass
    @abstractmethod
    def scale(self):
        pass