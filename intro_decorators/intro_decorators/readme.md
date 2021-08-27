```python
import time

def slow_square(number):
    print(f"Sleeping for {number} seconds")
    time.sleep(number)
    return number**2

print(slow_square(2))
```

```python
print(functools.lru_cache) #<function lru_cache at 0x108fcd560>
```