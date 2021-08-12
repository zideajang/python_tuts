import random

FUNCTIONS = {}

def register(func):
    FUNCTIONS[func.__name__] = func
    return func

@register
def roll_dice():
    return random.randint(1,6)


print(FUNCTIONS)


print(FUNCTIONS['roll_dice']())