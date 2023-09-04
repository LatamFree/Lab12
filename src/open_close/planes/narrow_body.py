from .plane import Plane

class NarrowBody(Plane):
    def __init__(self):
      self._type = 'NarrowBody'
    
    @property
    def type(self):
       return self._type
    
    def __str__(self):
       return f"{self.model}"