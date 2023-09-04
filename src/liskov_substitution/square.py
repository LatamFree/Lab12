from .rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self._width = self.width
        self._height = self.height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self._height = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self._width = value
