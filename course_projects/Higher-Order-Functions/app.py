def greet():
  print("Hi")

def before_and_after(func):
  print('Before...')
  func()
  print('...After')

before_and_after(lambda: print(10))

movies = [
  {'name': 'Klaus', 'director': 'Pablos'},
  {'name': 'The Matrix', 'director': 'Wachowski'},
  {'name': '1917', 'director': 'Mendes'},
]

def find_movie(expected, finder):
  for movie in movies:
  #   print(finder(movie))
    if finder(movie) == expected:
      return movie

find_by = input('What property ae we searching by?')
looking_for = input('What are you looking for?')
movie = find_movie(looking_for, lambda movie: movie[find_by])
print(movie or 'No movies found')