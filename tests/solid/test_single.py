import unittest
from src.single import Plane, PlaneDB      

class TestSuite(unittest.TestCase):
    def setUp(self):
       self.plane = Plane('787')
       
    def test_model(self):
        assert self.plane.model == '787'
    
    def test_db(self):
        assert self.plane.db.__class__ == PlaneDB
    
    def test_save_plane(self):
        assert self.plane.save() == f"Saved {self.plane} to database"
    
        
    