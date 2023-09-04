import unittest
from src.dependency_inversion.fleet.presenter import Presenter       
from src.dependency_inversion.fleet.db import DB       
from src.dependency_inversion.fleet.rest_api import RestAPI       


def test_with_db(capsys):
  # Given
  connection_str = "postgres://YourUserName:YourPassword@YourHostname:5432/YourDatabaseName"
  db = DB(connection_string=connection_str)
  presenter = Presenter(source=db)
  # When
  presenter.display()
  # Then
  captured = capsys.readouterr()  
  assert captured.out == f"Data from the DB with {connection_str}\n"
  
def test_with_api(capsys):
  url = "https://apis.latam.com/v1/fleet"
  rest_api = RestAPI(url)
  presenter = Presenter(rest_api)
  presenter.display() 
  captured = capsys.readouterr()  
  assert captured.out == f"Data from the API at url {url}\n"