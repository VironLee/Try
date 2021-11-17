class Position:
    __x: int
    __y: int

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def moveTo(self, des_x: int, des_y: int):
        self.__x = des_x
        self.__y = des_y

    def getXValue(self) -> int:
        return self.__x

    def getYValue(self) -> int:
        return self.__y
