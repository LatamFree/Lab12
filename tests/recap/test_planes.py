import unittest
from src.recap.narrow_body import NarrowBody       
from src.recap.wide_body import WideBody       
from src.recap.freighter import Freighter       

class TestSuite(unittest.TestCase):
    def setUp(self):
       self.narrow = NarrowBody()
       self.wide = WideBody()
       self.freighter = Freighter()

    def test_required_attributes(self):
        assert self.narrow.type == 'NarrowBody'
        assert self.wide.type == 'WideBody'
        assert self.freighter.type == 'Freighter'
        
    