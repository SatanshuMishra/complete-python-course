from typing import final


class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'


class Garage:
  def __init__(self):
    self.cars = []
    
  def __len__(self):
    return len(self.cars)

  def add_car(self, car):
    if not isinstance(car, Car):
      raise TypeError(f"Tried to add a '{car.__class__.__name__}' to the garage, but you can only add 'Car' objects.")
    self.cars.append(car)

ford = Garage()
f150 = Car("Ford", "F-150")
fiesta = Car("Ford", "Fiesta")
tahoe = "Tahoe"

# ASK PERMISSION AND THEN FORGIVENESS APPROCH
# if isinstance(f150, Car):
#   ford.add_car(f150)
# else:
#   print("You vehicle was not of type 'Car'!")

# ASK FORGIVENESS APPROCH
ford.add_car(f150)
ford.add_car(fiesta)
print(ford.cars)

try:
  # ford.add_car(tahoe)
  ford.add_car(fiesta)
except TypeError:
  print("Your vehicle was not of the type 'Car'!")
except ValueError:
  print("Something weird happend...")
else:
  print("No error occured...") # Will run only if no error occurs or nothing is returned above
finally:
  # WILL ALWAYS RUN AT THE END
  print(f"The garage has now {len(ford)} cars!")