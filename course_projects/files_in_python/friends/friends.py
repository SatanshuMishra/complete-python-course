friends = []
for friend in range(0, 3):
  friends.append(input("Enter the name of a friend: "))

# CAN USE str.split(',') AS WELL

my_file = open('people.txt', 'r')
# people_nearby = my_file.readlines() #IMPLEMENTATION 1
people_nearby = [line.strip() for line in my_file.readlines()] #IMPLEMENTATION 2
my_file.close()

friends_set = set(friends)
# people_nearby_set = set() #IMPLEMENTATION 1
people_nearby_set = set(people_nearby) #IMPLEMENTATION 2

# for person in people_nearby: #IMPLEMENTATION 1
#   people_nearby_set.add(person.removesuffix('\n'))


friends_nearby_set = people_nearby_set.intersection(friends_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for people in friends_nearby_set:
  nearby_friends_file.write(f"{people}\n")

nearby_friends_file.close()
