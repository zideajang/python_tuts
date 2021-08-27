import random

FUNCTIONS = {}

def register(func):
    FUNCTIONS[func.__name__] = func
    return func

def do_twice(func):
    def wrapper(*args,**kwargs):
        val_1 = func(*args,**kwargs)
        val_2 = func(*args,**kwargs)
        return (val_1,val_2)
    return wrapper 

@register
@do_twice
def roll_dice():
    return random.randint(1,6)

register = register(do_twice(roll_dice))

# print(roll_dice())
print(register)
print(FUNCTIONS["wrapper"]())