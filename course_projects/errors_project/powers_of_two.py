def power_of_two():
  n = input("Enter a number: ")
  try:
    n_float = float(n)
    return n_float ** 2
  except ValueError:
    print(f"Invalid Input! Cannot convert {n.__class__.__name__} to float value!")
    return 0

print(power_of_two())