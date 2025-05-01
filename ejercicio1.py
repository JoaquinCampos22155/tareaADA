import random
from math import log2, ceil

def random_bit():
    return random.randint(0, 1)  

def random_ab(a, b):
    n = b - a + 1
    k = ceil(log2(n))  # número mínimo de bits necesarios para cubrir el rango
    
    while True:
        r = 0
        for _ in range(k):
            r = (r << 1) | random_bit()
        if r < n:
            return a + r  
for _ in range(10):
    print(random_ab(3, 9))
