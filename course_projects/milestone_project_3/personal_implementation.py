import requests
from bs4 import BeautifulSoup
import json
  
page = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(page.content, 'html.parser')
locator = 'div.container div.row div.col-md-8 div.quote'
list_of_quotes = soup.select(locator)

quotes = []

for quote in list_of_quotes:
  sub_list = quote.findChildren('span')
  quote_text = sub_list[0].string
  quote_author = sub_list[1].findChildren('small')[0].string
  quotes.append(
    {
      'quote': quote_text,
      'author': quote_author
    }
  )

with open('quotes_scrpped.txt', 'w') as file:
  json.dump(quotes, file)