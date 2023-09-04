class PlaneDB():
    def save(self,plane):
       return f"Saved {plane} to database"
    # pass

class Plane: #Composición
  def __init__(self,model):
      self.model = model
      self.db = PlaneDB()
  
  def __repr__(self):
      return f"Plane(model={self.model})"

  def save(self): #Delegación
     return self.db.save(self)