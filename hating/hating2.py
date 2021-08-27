import random
import json

def init():
    return json.load(open('hating/data.json'))

data = init()["basic letters"]
data2 = ["A","D","C","B","E"]

def mutate(genom):
   r,r2 = (random.randint(0,len(genom)-1),random.randint(0,len(genom)-1))
   while r == r2:
       rand2 = random.randint(0,len(genom)-1)
   swap = genom[r]
   genom[r] = genom[r2]
   genom[r2] = swap

   return genom
