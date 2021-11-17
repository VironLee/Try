from position import Position


class Animal:
    weight: int
    name: str
    pos: Position

    def __init__(self, weight: int, name: str, pos: Position):
        self.weight = weight
        self.name = name
        self.pos = pos

    def moveTo(self, des_x: int, des_y: int):
        self.pos.moveTo(des_x, des_y)

    def fitting(self):
        self.weight -= 1

    def showWeight(self):
        print(self.name + "'s current weight is " + str(self.weight))

    def eat(self, food: int):
        self.weight += food


class Cat(Animal):

    def __init__(self, weight: int, name: str, pos: Position):
        Animal.__init__(self,weight, name, pos)

    def showCatPos(self):
        posX = self.pos.getXValue()
        posY = self.pos.getYValue()
        print("Cat " + self.name + " current position is (" + str(posX) + "," + str(posY) + ")")

    def bark(self):
        print("mia mia mia!")


class Dog(Animal):

    def __init__(self, weight: int, name: str, pos: Position):
        Animal.__init__(self,weight, name, pos)

    def showDogPos(self):
        posX = self.pos.getXValue()
        posY = self.pos.getYValue()
        print("Dog " + self.name + " current position is (" + str(posX) + "," + str(posY) + ")")

    def bark(self):
        print("wow wow wow!")
