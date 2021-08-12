import time
import functools

@functools.lru_cache(maxsize=128, typed=False)
def slow_square(number):
    print(f"Sleeping for {number} seconds")
    time.sleep(number)
    return number**2

print(slow_square(3))
print(slow_square(3))
print(slow_square(3))


print(functools.lru_cache) #<function lru_cache at 0x108fcd560>