import json

file = open("friends_json.txt", "r")
file_contents = json.load(file) # READS FILE AND TURNS CONTENT TO A DICTIONARY
file.close()

print(file_contents['friends'][0])

cars = [
  {'make': 'Ford', 'model': 'F-150'},
  {'make': 'Cheverlet', 'model': 'Tahoe'}
]

file = open("cars_json.txt", "w")
json.dump(cars, file)
file.close()

my_json_string = '{"name": "Rolf Smith", "age": 23}'
incorrect_car = json.loads(my_json_string)
print(incorrect_car)

