import random
import json

f = json.load(open('hating/data.json'))

data = f["basic letters"]
data2 = ["A", "D", "C", "B", "E"]


def mutate(genom):
    r, r2 = (random.randint(0, len(genom)-1), random.randint(0, len(genom)-1))
    while r == r2:
        rand2 = random.randint(0, len(genom)-1)
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


    
