class Dog:  # 创建一个虚拟类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} rolled over,it was {self.age}')


class Dog:  # 实例化
    my_dog = Dog('whitle', 8)
    your_dog = Dog('black', 2)
    my_dog.sit()
    your_dog.sit()
    your_dog.roll_over()
    my_dog.roll_over()