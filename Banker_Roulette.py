#Banker Roulette is a simple program that randomly selects a friend from a list of friends.

#1 List of friends
friends = ["Alice", "Bob", "Charlie", "David", "Eve"]
# Different oprtions to code.


#Options 1
import random
print(random.choice(friends))


# Options 2
random_index =random.randint(0, 4)
print(friends[random_index])

