from .plane import Plane

class Freighter(Plane):
    def __init__(self):
      self._type = 'Freighter'
    
    @property
    def type(self):
       return self._type
    
    def __str__(self):
       return f"{self.model}"    