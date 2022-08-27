import re
import logging
from bs4 import BeautifulSoup
from locators.books_page_locator import BooksWebpageLocator
from parsers.book import BookParser

logger = logging.getLogger('scraping.books_page')


class BooksPage:
  def __init__(self, page) -> None:
    logger.debug('Parsing page content with BeautifulSoup HTML parser.')
    self.soup = BeautifulSoup(page, 'html.parser')

  @property
  def books(self):
    locator = BooksWebpageLocator.BOOKS
    logger.debug(f'Finding all books in page using `{locator}`.')
    book_tags = self.soup.select(locator)
    return [BookParser(b) for b in book_tags]

  @property
  def page_count(self):
    logger.debug('Finding all number of catalogue pages available...')
    locator = BooksWebpageLocator.PAGER
    content = self.soup.select_one(locator).string

    logger.info(f'Found number of catalogue pages available: `{content}`')

    expression = 'Page [0-9]+ of ([0-9]+)'
    matcher = re.search(expression, content)
    pages = int(matcher.group(1))

    logger.debug(f'Extracted the number of pages as integer value: `{pages}`')
    
    return pages
