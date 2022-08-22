from msilib import sequence
import sqlite3

class DatabaseConnection:
  def __init__(self, host):
    self.connection = None
    self.host = host
  
  def __enter__(self) -> sqlite3.Connection:
    self.connection = sqlite3.connect(self.host)
    return self.connection

  def __exit__(self, exc_type, exc_val, exc_tb):
    # IF STATEMENT TO CLOSE WHENEVER AN EXCEPTION OCCURS - DISABLED DUE TO A TRY-EXCEPT BEING IMPLIMENTED
    # if exc_type or exc_val or exc_tb:
    #   self.connect.close()
    # else:
      self.connection.commit()
      self.connection.close()
    