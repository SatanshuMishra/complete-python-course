from this import d
from xml.sax.xmlreader import Locator
from bs4 import BeautifulSoup
from locators.quotes_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser

class QuotesPage:
  def __init__(self, page) -> None:
    self.soup = BeautifulSoup(page, 'html.parser')

  @property
  def quotes(self):
    locator = QuotesPageLocators.QUOTES
    quote_tags = self.soup.select(locator)
    return [QuoteParser(e) for e in quote_tags]