MENU_PROMPT = """
Please select a numberical value below:
1: Add a new movie
2: See your movies
3: Find a movie by title
Q: Quit App
"""

movies = []
selection = input(MENU_PROMPT)

def print_movie(movie, count = "N/A"):
    print(f"""
  Movie Number {count}:
  Title: {movie["title"]}
  Director: {movie["director"]}
  Year of Release: {movie["release_year"]}
  """)

while selection != "Q":
  if selection == "1":
    movies.append({
      "title": input("Enter movie title: "),
      "director": input("Enter movie director: "),
      "release_year": input("Enter movie release year: ")
    })
  elif selection == "2":
    for count, movie in enumerate(movies, start = 1):
      print_movie(movie, count)
  elif selection == "3":
    search_title = input("Enter name of movie: ")
    for movie in movies:
      if movie["title"] == search_title:
        print_movie(movie)
        break
    else:
      print(f"We didn't find any movie by the name '{search_title}'")

  selection = input(MENU_PROMPT)