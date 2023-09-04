from .polygon import Polygon

class Square(Polygon):
    def __init__(self, side):
        self.side = side

    def calculate_area(self):
        return self.side**2
    
    def scale(self, factor):
        self.side*=factor


    #     self._height = self.height

    # @property
    # def width(self):
    #     return self._width

    # @width.setter
    # def width(self, value):
    #     self._width = value
    #     self._height = value

    # @property
    # def height(self):
    #     return self._height

    # @height.setter
    # def height(self, value):
    #     self._height = value
    #     self._width = value
