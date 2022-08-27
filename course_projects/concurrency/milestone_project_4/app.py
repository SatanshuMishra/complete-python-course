import aiohttp
import asyncio
import async_timeout
import time
import requests
import logging
from pages.books_page import BooksPage

logging.basicConfig(
  format='%(asctime)s %(levelname)-8s [%(filename)s: %(lineno)d] %(message)s',
  datefmt='%d-%m-%y %H:%M:%S', 
  level=logging.DEBUG,
  filename='logs.txt'
)

logger = logging.getLogger('scraping')

logger.info('Loading books list...')

page_content = requests.get('https://books.toscrape.com/').content
page = BooksPage(page_content)


loop = asyncio.get_event_loop()

books = page.books

async def fetch_page(session, url):
  page_start = time.time()
  async with session.get(url) as response:
    print(f'The page took {time.time() - page_start}')
    return await response.text()

async def get_multiple_pages(loop, *urls):
  tasks = []
  async with aiohttp.ClientSession(loop = loop) as session:
    for url in urls:
      tasks.append(fetch_page(session, url))
    grouped_tasks= asyncio.gather(*tasks)
    return await grouped_tasks 

urls = [f'https://books.toscrape.com/catalogue/page-{i + 1}.html' for i in range(page.page_count)]
start = time.time()
pages = loop.run_until_complete(get_multiple_pages(loop, *urls))

print(f'Total Page Requests Time: {time.time() - start}')

for page_content in pages:
  logger.debug('Creating BooksPage from page content.')
  page = BooksPage(page_content)
  books.extend(page.books)

