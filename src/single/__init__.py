class PlaneDB():
    pass

class Plane:
  def __init__(self,model):
      self.model = model
  
  def __repr__(self):
      return f"Plane(model={self.model})"

  def save(self):
     return f"Saved {self} to database"