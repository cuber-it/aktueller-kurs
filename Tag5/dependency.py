class Walker:
    def walk(self):
        print("Walking...")

class Swimmer:
    def swim(self):
        print("Swimming...")

class Flyer:
    def fly(self):
        print("Flying...")

class Animal:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("I am", self.name)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.walker = Walker()
        self.swimmer = Swimmer()

    def walk(self):
        self.walker.walk()

    def swim(self):
        self.swimmer.swim()

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walk(self):
        Walker().walk()

    def fly(self):
        Flyer().fly()

dog = Dog("Lilly")
dog.walk()   # Output: Walking...
dog.swim()   # Output: Swimming...
dog.hello()

bird = Bird("Birdie")
bird.walk()  # Output: Walking...
bird.fly()   # Output: Flying...
bird.hello()
