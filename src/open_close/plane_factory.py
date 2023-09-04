from inspect import getmembers, isclass, isabstract
import src.open_close.planes as planes

class PlaneFactory:
  planes = {

  }
  def __init__(self) -> None: #__init__ es cuando se crea una instancia
    self.load_planes()

  def load_planes(self):
    classes = getmembers(
      planes,
      lambda p: isclass(p) and not isabstract(p)
    )
    for name, type in classes:
      if issubclass(type,planes.Plane):
        self.planes[name] = type

  def create(self, type):
    if type in self.planes:
      return self.planes[type]()
    else:
      raise TypeError