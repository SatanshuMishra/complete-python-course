import time
import random
import queue

from threading import Thread

counter = 0
job_queue = queue.Queue() # THINGS TO BE PRINTED OUT
counter_queue = queue.Queue() # AMOUNTS BY WHICH TO INCREASE COUNTER

def increment_manager():
  global counter
  while True:
    increment = counter_queue.get() # THIS WAITS UNTIL AN ITEM IS AVAILABLE THEN LOCKS THE QUEUE
    time.sleep(random.random())
    old_counter = counter
    counter = old_counter + increment
    time.sleep(random.random())
    job_queue.put((f'The new counter value is {counter}', "----------"))
    time.sleep(random.random())
    time.sleep(random.random())
    counter_queue.task_done() # THIS UNLOCKS THE QUEUE
Thread(target=increment_manager, daemon=True).start()

def printer_manager():
  time.sleep(random.random())
  while True:
    for line in job_queue.get():
      print(line)
      time.sleep(random.random())
    job_queue.task_done()
    time.sleep(random.random())
Thread(target=printer_manager, daemon=True).start()

def increment_counter():
  counter_queue.put(1)

worker_threads = [Thread(target=increment_counter) for thread in range(10)]

for thread in worker_threads:
  thread.start()

for thread in worker_threads:
  thread.join()

counter_queue.join()
job_queue.join()