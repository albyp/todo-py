import sqlite # does this need to be done here or app.py

class Schema:
  def __init__(self):
    self.conn = sqlite3.connect('todo.db')
    self.create_todo_table()
    self.create_user_table() # test with todo table first to see the error
  
  def create_todo_table(self):
    
    query = """
    CREATE TABLE IF NOT EXISTS "Todo" (
      id INTEGER PRIMARY KEY,
      Title TEXT,
      Description TEXT,
      _is_done boolean,
      _is_deleted boolean,
      CreatedOn Date DEFAULT CURRENT_DATE,
      DueDate Date,
      UserID INTEGER FOREIGNKEY REFERENCES User(_id)
    );
    """
    
    self.conn.execute(query)
    
  def create_user_table(self):
    
    query = """
    CREATE TABLE IF NOT EXISTS "User" (
      id INTEGER PRIMARY KEY,
      Name TEXT,
    )
    """
    
    self.conn.execute(query)
