"""
CONCERNED WITH STORING THE DATABASE
"""
from typing import Dict, List, Union
from .database_connection import DatabaseConnection

import sqlite3

Book = Dict(str, Union(str, int))

def create_book_table() -> None:
  with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')

def add_book(name: str, author: str) -> None:
  try:
    with DatabaseConnection('data.db') as connection:
      cursor = connection.cursor()
      cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))

    print(f"🔔 Added {name} by {author} to the store!")
  except sqlite3.IntegrityError:
    print(f"The book '{name}' already exists!")

def mark_read(name: str) -> None:
  if find_book(name):
    with DatabaseConnection('data.db') as connection:
      cursor = connection.cursor()
      cursor.execute("UPDATE books SET read=1 WHERE name=?", (name,))
  else:
    print(f"The book '{name}' doesn't exist!")
  
def list_books() -> None:
  with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()] # [(name, author, read), ...]

  if books:
    print("List of currently stored books: ")
    for book in books:
      read = "YES" if book['read'] else "NO"
      print(f"📖 {book['name']} by {book['author']}; Read: {read}")
  else:
    print('Store is Empty!')

# HELPER METHOD TO CHECK IF A BOOK EXISTS
def find_book(name: str) -> List[Book]:
  with DatabaseConnection('data.db') as connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE name=?", (name,))
    book = cursor.fetchall()
    
  return book
  
def delete_book(name: str) -> None:
  if find_book(name):
    with DatabaseConnection('data.db') as connection:
      cursor = connection.cursor()
      cursor.execute("DELETE FROM books WHERE name=?", (name,))
  else:
    print(f"The book '{name}' doesn't exist!")
