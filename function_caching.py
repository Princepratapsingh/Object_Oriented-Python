from functools import lru_cache
import time
@lru_cache(maxsize=None)
def multiply(n):
    time.sleep(5)
    return n*5

print(multiply(10))
print(multiply(11))
print(multiply(12))
print(multiply(10))
print(multiply(11))
print(multiply(12))
print(multiply(15))
    
