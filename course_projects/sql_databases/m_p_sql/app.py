from utils import database

USER_CHOICE = """
Choose an option below:
- 'a' to add new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
  database.create_book_table()
  user_input = input(USER_CHOICE)
  while user_input != 'q':
# def prompt_add_book() # ASK FOR BOOK NAME AND AUTHOR
    if user_input == 'a':
      name = input("Enter book's name: ") 
      author = input("Enter author's name: ") 
      database.add_book(name, author)
# def list_books() # SHOW ALL BOOKS IN OUR LIST
    elif user_input == 'l':
      database.list_books()
# def prompt_read_book() # ASK FOR BOOK NAME AND CHANGE IT TO READ IN OUR LIST
    elif user_input == 'r':
      name = input("Enter book's name: ")
      database.mark_read(name)
# def prompt_delete_book() # ASK FOR BOOK NAME AND REMOVE IT FROM LIST
    elif user_input == 'd':
      name = input("Enter book's name: ")
      database.delete_book(name)
    else:
      print("Unknown command. Please try again.")

    user_input = input(USER_CHOICE)


menu()