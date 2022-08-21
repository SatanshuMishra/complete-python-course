import json

with open("friends_json.txt", "r") as file:
  file_contents = json.load(file)

print(file_contents['friends'][0])

cars = [
  {'make': 'Ford', 'model': 'F-150'},
  {'make': 'Cheverlet', 'model': 'Tahoe'}
]

with open("cars_json.txt", "w") as file:
  json.dump(cars, file)


my_json_string = '{"name": "Rolf Smith", "age": 23}'
incorrect_car = json.loads(my_json_string)
print(incorrect_car)

