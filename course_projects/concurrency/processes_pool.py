from concurrent.futures import ProcessPoolExecutor
import time

####### SINGLE PROCESS

def ask_user():
	start = time.time()
	user_input = input('Enter your name: ')
	greet = f'Hello, {user_input}'
	print(greet)
	print('ask_user: ', time.time() - start)

def complex_calculation():
	print('Started calculating...')
	start = time.time()
	[x**2 for x in range(20000000)]
	print('complex_calculation: ', time.time() - start)


####### TWO PROCESSES


start = time.time()
if __name__ == "__main__":
  
  with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(complex_calculation)
    pool.submit(complex_calculation)

  print('Two process total time: ', time.time() - start)
