#Random Module

import random

k=random.random()
print(k)

l=random.uniform(1,10)
print(l)

m=random.randint(1,5)
print(m)

greetings=['Hi','Hello','Howdy','Hola','Hey']

n=random.choice(greetings)
print(n)

deck=list(range(1,53))
random.shuffle(deck)
print(deck)

hand=random.sample(deck,5)
print(hand)

