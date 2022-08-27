from ast import Str
from collections import deque
friends = deque(('Rolf', 'Anne', 'Jen'))

def get_friend() -> str:
  yield from friends

def greet(g) ->str:
  while True:
    try:
      friend = next(g)
      yield f'Hello {friend}'
    except StopIteration:
      pass

friends_gen = get_friend()
g = greet(friends_gen)
print(next(g))
print(next(g))
print(next(g))