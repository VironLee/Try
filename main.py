from animal import Cat, Dog
from position import Position

if __name__ == '__main__':



    #声明一个叫kitty的猫
    posCat=Position(5,6) #先调用Position构造函数， 生成一个position对象posCat
    cat_Kitty = Cat(10, 'Kitty',posCat) #posCat作为参数输入到Cat构造函数里

    #声明一个叫andrew的狗
    dog_Andrew = Dog(20, 'Andrew',Position(7,10)) #直接在Dog构造函数对应position类型的位置，调用Position构造函数生成一个Position对象，作为Cat构造函数的输入
    ###由此可见，声明一个类和声明一个变量很相似


    #直接访问动物的名字，
    #名字这个属性只定义在Animal类下面，在cat和dog下面均没有定义
    #说明子类可以直接通过.取得父类的属性
    print("print names of animals:")
    print(cat_Kitty.name)
    print(dog_Andrew.name)
    print("")

    # 调用cat和dog这两个子类自己的方法
    # bark（）各自定义在cat和dog类下面，不是animal的父类方法，执行效果也根据具体的类而不同

    cat_Kitty.bark()
    dog_Andrew.bark()
    print("")

    #复杂场景，减肥
    #这里fitting()和showWeight()都是Animal的父类方法，说明子类的对象可以调用父类的方法
    cat_Kitty.fitting()
    print("cat减肥后：")
    cat_Kitty.showWeight()
    print("")

    dog_Andrew.eat(5)
    print("dog 吃胖了：")
    dog_Andrew.showWeight()
    print("")
    #类的方法定义顺序不影响程序执行的效果

    #moveTo
    dog_Andrew.moveTo(19,2)
    cat_Kitty.moveTo(30,40)

    #查看moveTo后动物的坐标
    cat_Kitty.showCatPos()
    dog_Andrew.showDogPos()