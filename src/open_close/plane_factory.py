from inspect import getmembers, isclass, isabstract
from src.open_close.planes import *

class PlaneFactory:
  @classmethod
  def create(cls,type):
    match type:
      case "NarrowBody":
        return NarrowBody()
      case "WideBody":
        return WideBody()
      case "Freighter":
        return Freighter()
      case _:
        raise TypeError
