from animal import Animal
from map import Map

if __name__ == '__main__':
    map = Map(6, 7)

    #声明一个叫cat的动物类
    cat = Animal(10, 'cat')

    #声明一个叫dog的动物类
    dog = Animal(20, 'dog')

    ###可以发现声明一个类和声明一个变量很相似

    # 调用类的方法
    cat.bark()
    dog.bark()

    #复杂场景，减肥
    cat.fitting()
    print("cat减肥后：")
    cat.showWeight()

    dog.eat(5)
    print("dog 吃胖了：")
    dog.showWeight()

