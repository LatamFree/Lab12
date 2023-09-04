import unittest
from src.liskov_substitution.square import Square, Rectangle     

class TestSuite(unittest.TestCase):
    def setUp(self):
       self.rectangle = Rectangle(2,3)
       self.square = Square(2)
       
    def test_rectangle_area(self):
        assert self.rectangle.calculate_area() == 6

        self.rectangle.width = 3
        assert self.rectangle.calculate_area() == 9
        
    def test_square_area(self):
        assert self.square.calculate_area() == 4

        self.square.width = 3
        assert self.square.calculate_area() == 9

    def test_scale_shapes(self):
        self.rectangle.scale(2) # scale from 2,3 to 4,6
        assert self.rectangle.calculate_area() == 24


        self.square.scale(2) # scale from 2,2 to 4,4

        assert self.square.calculate_area() == 16
