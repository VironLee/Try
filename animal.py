class Animal:
    weight: int
    name: str

    def __init__(self, weight:int, name: str):
        self.weight = weight
        self.name = name

    def bark(self):
        print("hello ,I am " + self.name)

    def fitting(self):
        self.weight -= 1

    def showWeight(self):
        print(self.name + "'s current weight is " + str(self.weight))

    def eat(self,food:int):
        self.weight+=food