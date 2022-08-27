import time
from concurrent.futures import ThreadPoolExecutor
def ask_user():
  start = time.time()
  user_input = input("Enter your name: ")
  print(f"Hello, {user_input}")
  end = time.time()
  print(f'Time taken (Greet): {time.time() - start}')
def complex_calculation():
  print('Started Calculating...')
  start = time.time()
  [x**2 for x in range(20000000)]
  print(f'Time taken (Calc): {time.time() - start}')

start = time.time()
ask_user()
complex_calculation()
print(f'Time taken (Whole): {time.time() - start}')

start = time.time()

with ThreadPoolExecutor(max_workers=2) as pool:
  pool.submit(complex_calculation)
  pool.submit(ask_user)

print(f'Time taken (Thread(s)): {time.time() - start}')