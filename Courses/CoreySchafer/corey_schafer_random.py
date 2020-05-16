import random

value=random.randint(1, 5)
print(value)

value=random.random()
print(value)

colors=['Red', 'Black', 'Green']
results=random.choices(colors, weights=[4,3,2], k=10)
print(results)

deck=list(range(1,53))
random.shuffle(deck)
print(deck)

hand=random.sample(deck, k=5)
print(hand)