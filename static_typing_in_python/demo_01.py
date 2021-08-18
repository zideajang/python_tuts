import random
a = random.choice([42,42.0, '42'])
print(type(a))

def guessType(a,b,c):
    return a + b + c

guessType(1,2.0,'foo')