from addition import Addition

class Calculator:
  @classmethod
  def add(cls, num1, num2):
    return Addition.add(num1, num2)
  
  @classmethod
  def subtract(cls, num1, num2):
    return Addition.add(num1, -num2)

  @classmethod
  def multiply(cls, num1, num2):
    result = 0
    for i in range(0, num2):
      result = Addition.add(result, num1)
    return result

  @classmethod
  def divide(cls, num1, num2):
    number = num1
    counter = 0
    while number != 0:
      if Addition.add(number, -num2) < 0:
        return counter
      number = Addition.add(number, -num2)
      counter = Addition.add(counter, 1)
    return counter

print(Calculator.divide(12, 4))
print(Calculator.divide(11, 4))
print(Calculator.subtract(11, 4))
print(Calculator.add(11, 4))
print(Calculator.multiply(2, 4))