import random

def do_twice(func):
    def wrapper(*args,**kwargs):
        val_1 = func(*args,**kwargs)
        val_2 = func(*args,**kwargs)
        return (val_1,val_2)
    return wrapper

@do_twice
def roll_dice():
    return random.randint(1,6)


print(roll_dice())