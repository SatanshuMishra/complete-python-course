import re
import logging
from locators.book_locator import BookLocator

logger = logging.getLogger("scraping.book_parsing")

class BookParser:

  RATINGS = {
    'One': 1,
    'Two': 2,
    'Three': 3,
    'Four': 4,
    'Five': 5
  }

  def __init__(self, parent) -> None:
    logger.debug(f'New book parser created from `{parent}`')
    self.parent = parent

  def __repr__(self) -> str:
    return f"""
    Name: {self.title}
    Price: {self.price}
    Rating: {self.rating} ✨
    URL: {self.link}
    """

  @property
  def title(self):
    logger.debug('Finding a book name...')
    locator = BookLocator.TITLE
    title = self.parent.select_one(locator).attrs.get('title')
    logger.debug(f'Found book name, `{title}`')
    return title

  @property
  def price(self):
    logger.debug('Finding a book price...')
    locator = BookLocator.PRICE
    price_tag = self.parent.select_one(locator).string
    pattern = '£([0-9]+\.[0-9])+'
    matches = re.match(pattern, price_tag)
    price = float(matches.group(1))
    logger.debug(f'Found book price, `{price}`')
    return price

  @property
  def rating(self):
    logger.debug('Finding a book rating...')
    locator = BookLocator.RATING
    classes = self.parent.select_one(locator).attrs.get('class')
    rating_string = [r for r in classes if r != 'star-rating'][0]
    rating = BookParser.RATINGS[rating_string]
    logger.debug(f'Found book rating, `{rating}`')
    return rating

  @property
  def link(self):
    logger.debug('Finding a url to book...')
    locator = BookLocator.LINK
    url = self.parent.select_one(locator).attrs.get('href')
    logger.debug(f'Found book link, `{url}`')
    return url
