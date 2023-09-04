import unittest
import pytest
from src.open_close.plane_factory import PlaneFactory       

class TestSuite(unittest.TestCase):   
  def setUp(self):
    self.factory = PlaneFactory()
  def test_type(self):
    for type in ["NarrowBody","WideBody","Freighter"]:
      assert self.factory.create(type).type == type
  
  def test_other_type(self):
    with pytest.raises(TypeError):
      PlaneFactory.create('Other')
