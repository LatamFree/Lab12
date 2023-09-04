from .plane import Plane

class WideBody(Plane):
    def __init__(self):
      self._type = 'WideBody'
    
    @property
    def type(self):
       return self._type
    
    def __str__(self):
       return f"{self.model}"