from .db import DB

class Presenter:
  def __init__(self,source):
    self.source = source
    self.db = DB("cnxstr...")

  def display(self):
    data =  self.source.get_data()
    print(data)