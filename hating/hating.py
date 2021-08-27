import json
import random

d = json.load(open('data.json'))
connections = d["connections"]

def init() -> list:
    s = d["basic letters"]
    random.shuffle(s)
    return s

def getHate(a: str, b: str) -> int:
    """
    >>> getHate("C", "E")
    14
    >>> getHate("C", "A")
    11
    """
    for con in connections:
        if {a, b} == set(con["letters"]):
            return con["value"]
    return 0

def fitness(genom) -> int: 
    """
    >>> fitness(["A", "B", "C", "D", "E"])
    8
    """
    sum = 0
    for i in range(len(genom) - 1):
        sum += getHate(genom[i], genom[i+1])
    return sum

def mutate(genom) -> list:
    r,r2 = (random.randint(0,len(genom)-1),random.randint(0,len(genom)-1))
    while r == r2:
        rand2 = random.randint(0,len(genom)-1)
    swap = genom[r]
    genom[r] = genom[r2]
    genom[r2] = swap
 
    return genom

if __name__ == "__main__":
    import doctest
    doctest.testmod()
