import logging
from app import books

logger = logging.getLogger('scraping.menu')

USER_CHOICE = '''Select one of the following choices:
- "b" to look at 5-star books
- "c" to look at the cheapest books
- "n" to get the next available book on the catalogue
- "q" to exit

Enter your choice: '''


# TO SORT BY MULTIPLE FACTORS, USE A TUPLE INSTEAD OF SINLGLE VALUES. THE FIRST FACTOR WILL BE USED FOR SORTING. IF ANY BOOKS ENCOUNTED WITH IDENTICAL VALUES FOR FIRST FACTOR, SECOND FACTOR WILL BE USED

# sorted(books, key=lambda book: (book.price, book.rating), reverse=False)


def print_best_rated_books():
  logger.info('Finding best books by rating...')
  best_books = sorted(books, key=lambda book: book.rating, reverse=True)[:10]
  for book in best_books:
    print(book)

def print_cheapest_books():
  logger.info('Finding cheapest books by price...')
  cheapest_books = sorted(books, key=lambda book: book.price, reverse=False)[:10]
  for book in cheapest_books:
    print(book)

books_generator = (x for x in books)
logger.info('Getting next book from generator of all books...')
def next_available_book():
  print(next(books_generator))


user_input = input(USER_CHOICE)
while(user_input != "q"):
  if user_input == "b":
    print_best_rated_books()
  elif user_input == "c":
    print_cheapest_books()
  elif user_input == "n":
    next_available_book()
  else:
    print('Please choose a valid command!')

  user_input = input(USER_CHOICE)
  