from locators.quote_locators import QuotesLocators

class QuoteParser:
  """
  Given one of the specific quote divs, find out data about the quotes (quote content, author, tags)
  """

  def __init__(self, parent) -> None:
    self.parent = parent

  def __repr__(self) -> str:
    return f'<Quote {self.content}, by {self.author}>'

  @property
  def content(self) -> str:
    locator = QuotesLocators.CONTENT
    return self.parent.select_one(locator).string

  @property
  def author(self) -> str:
    locator = QuotesLocators.AUTHOR
    return self.parent.select_one(locator).string

  @property
  def tags(self) -> list:
    locator = QuotesLocators.TAGS
    return [e.string for e in self.parent.select_one(locator).string]