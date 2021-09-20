import json
import random

d = json.load(open('hating/data.json'))
connections = d["connections"]

def init() -> list:
    s = d["basic letters"]
    random.shuffle(s)
    return s[:]

def init_gen():
    list = []
    for _ in range(100):
        list.append(init())
    return list

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
    >>> fitness(["A", "C", "B", "D", "E"])
    24
    >>> fitness(["E", "B", "D", "C", "A"])
    19
    >>> fitness(["C", "B", "D", "E", "A"])
    13
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

def crossover(genom, genom2):
    new_genom = genom[:2]

    while len(new_genom) != 5:
        r = random.randint(0, len(genom)-1)
        if genom2[r] not in new_genom:
            new_genom.append(genom2[r])

    return new_genom

def sort(genom_list: list):
    """
    >>> l = [["A", "B", "C", "D", "E"], ["A", "C", "B", "D", "E"], ["E", "B", "D", "C", "A"]]
    >>> sort(l)
    >>> l
    [['A', 'B', 'C', 'D', 'E'], ['E', 'B', 'D', 'C', 'A'], ['A', 'C', 'B', 'D', 'E']]
    """
    genom_list.sort(key=fitness)

def select(genom_list: list):
    """
    >>> l = [['A', 'B', 'C', 'D', 'E'], ['C', 'B', 'D', 'E', 'A'], ['E', 'B', 'D', 'C', 'A'], ['A', 'C', 'B', 'D', 'E']]
    >>> l = select(l)
    >>> l
    [['A', 'B', 'C', 'D', 'E'], ['C', 'B', 'D', 'E', 'A']]
    """
    return genom_list[:int(0.7 * len(genom_list))]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
