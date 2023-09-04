from .source import Source

class RestAPI(Source):
  def __init__(self,url):
    self.url = url

  def get_data(self):
    return f"Data from the API at url {self.url}"