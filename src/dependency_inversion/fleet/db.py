from .source import Source

class DB(Source):
  def __init__(self, connection_string):
    self.connection_string = connection_string
  
  def get_data(self):
    return f"Data from the DB with {self.connection_string}"