from bs4 import BeautifulSoup

SIMPLE_HTML='''
<html>
  <head></head>
  <body>
    <h1>This is a header</h1>
    <p class="subtitle">This is a subtitle</p>
    <ul>
      <li>Rolf</li>
      <li>Charles</li>
      <li>Anne</li>
      <li>Kate</li>
    </ul>
    <p>This is a subtitle</p>
  </body>
<html>
'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')

def find_title():
  print(simple_soup.find('h1').string)

def find_list_items():
  list_items = simple_soup.find_all('li')
  list_items = [item.string for item in list_items]
  print(list_items)

def find_subtitle():
  pragraph = simple_soup.find('p', {'class': 'subtitle'})
  print(pragraph.string)

def find_other_paragraph():
  paragraphs = simple_soup.find_all('p')
  other_paragraph = [p for p in paragraphs if 'subtitle' not in p.attrs.get('class', [])]
  print(other_paragraph)
find_title()
find_list_items()
find_subtitle()
find_other_paragraph()