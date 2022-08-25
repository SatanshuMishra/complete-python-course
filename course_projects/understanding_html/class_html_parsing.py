import re
from bs4 import BeautifulSoup
ITEM_HTML = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
  <article class="product_pod">
    <div class="image_container">
      <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
    </div>
    <p class="star-rating Three">
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
      <i class="icon-star"></i>
    </p>
    <h3>
      <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a>
    </h3>
    <div class="product_price">
      <p class="price_color">£51.77</p>
      <p class="instock availability">
        <i class="icon-ok"></i>
        In stock
      </p>
      <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
      </form>
    </div>
  </article>
</li>

</body></html>
'''

class ParsedItemLocators:
  """
    Locator for items in the HTML page.
    
    This allows us to easily see what our code wil be looking at as well as change it quickly if we notice it is now different.
  """
  NAME_LOCATOR = 'article.product_pod h3 a'
  LINK_LOCATOR = 'article.product_pod h3 a'
  PRICE_LOCATOR = 'article.product_pod div.product_price p.price_color'
  RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
  """
    A Class to take in an HTML page, and find peroperties of an item within.
  """
  def __init__(self, page) -> None:
    self.soup = BeautifulSoup(page, 'html.parser')

  @property
  def name(self):
    locator = ParsedItemLocators.NAME_LOCATOR # CSS LOCATOR
    item_name = self.soup.select_one(locator).attrs.get('title')
    return item_name

  @property
  def link(self):
    locator = ParsedItemLocators.LINK_LOCATOR # CSS LOCATOR
    item_link = self.soup.select_one(locator).attrs.get('href')
    return item_link

  @property
  def price(self):
    locator = ParsedItemLocators.PRICE_LOCATOR # CSS LOCATOR
    item_price = self.soup.select_one(locator).string
    pattern = '£([0-9]+\.[0-9]+)'
    matches = re.match(pattern, item_price)
    return float(matches.group(1))

  @property
  def rating(self):
    locator = ParsedItemLocators.RATING_LOCATOR
    classes = self.soup.select_one(locator).attrs.get('class')
    item_rating = [cl for cl in classes if cl != 'star-rating']
    # item_rating = filter(lambda x: x!= 'star-rating', classes)
    return item_rating[0]

pageA = ParsedItem(ITEM_HTML)
print(f"NAME: {pageA.name}")
print(f"LINK: {pageA.link}")
print(f"PRICE: {pageA.price}")
print(f"RATING: {pageA.rating}")