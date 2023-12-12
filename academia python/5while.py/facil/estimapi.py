

import math

def calcula_pi(n):
    i = 1
    dentro = 0
    while i<=n:
        dentro += 6/i**2
        i+=1
    pi = math.sqrt(dentro)
    return pi

print(calcula_pi(2))
