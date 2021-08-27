import json

class Genom:
    def __init__(self) -> None:
        d = json.load(open('data.json'))
        self.connections = d["connections"]
        self.letters = d["basic letters"]

    def getHate(self, a: str, b: str):
        for con in self.connections:
            if {a, b} == set(con["letters"]) and len(set(con["letters"])) == 2:
                return con["value"]

    def fitness(self): 
        pass

g = Genom()
print(g.getHate("A", "B"))
