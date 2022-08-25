from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from pages.quotes_page import QuotesPage, InvalidTagForAuthor
try:
    author = input("Enter the author you'd like quotes from: ")
    tag = input("Enter your tag: ")

    service = Service("C:\\Users\\satan\\Downloads\\chromedriver_win32\\chromedriver.exe")
    chrome = webdriver.Chrome(service=service)
    chrome.get("http://quotes.toscrape.com/search.aspx")
    page = QuotesPage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthor as e:
    print(e)
except Exception as e:
    print('An unknown error occurred. Please try again.')