from collections import deque
from types import coroutine

friends = deque(('Rolf', 'Anne', 'Kate', 'Jen', 'Bob'))

@coroutine
def friends_upper():
  while friends:
    friend = friends.popleft().upper()
    greeting = yield
    print(f'{greeting}, {friend}')

async def greet(g):
  print("Starting...")
  await g
  print("Ending...")

greeter = greet(friends_upper())
greeter.send(None)
greeter.send('HI')
print('Hello World! Multitasking...')
greeter.send('HOW ARE YOU')
greeter.send('HOW ARE YOU')
greeter.send('HOW ARE YOU')
greeter.send('HOW ARE YOU')

