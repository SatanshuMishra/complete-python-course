"""
CONCERNED WITH STORING THE DATABASE
"""
import json

# - 's' to store current list of books
# - 'o' to load list of stored books

books = []

def add_book(name, author):
  retrieve_books()
  book = {
    'name': name,
    'author': author,
    'read': False
  }
  books.append(book)
  print(f"🔔 Added {name} by {author} to the store!")
  store_books()

def mark_read(name):
  retrieve_books()
  for book in books:
    if name == book['name']:
      book['read'] = True
      print(f"🔔 Marked {book['name']} by {book['author']} as read!")
      store_books()
      return
  else:
    print(f"🔔 The book '{name}' was not found.")

  
def list_books():
  retrieve_books()
  print("List of currently stored books: ")
  for book in books:
    read = "YES" if book['read'] else "NO"
    print(f"📖 {book['name']} by {book['author']}; Read: {read}")

def find_book(name):
  for book in books:
    if book['name'] == name:
      return book
  
def delete_book(name):
  global books
  retrieve_books()
  if find_book(name):
    books = [book for book in books if book['name'] != name]
    print(f"🔔 Removed '{name}' from the store!")
    store_books()
  else:
    print(f"The book '{name}' doesn't exist!")

def store_books():
  with open("books.txt", "w") as file:
    json.dump(books, file)

def retrieve_books():
  global books
  try:
    with open("books.txt", "r") as file:
      books = json.load(file)
  except FileNotFoundError:
    file = open("books.txt", "w")
    file.close()