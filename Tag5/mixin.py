class WalkMixin:
    def walk(self):
        print("Walking...")

class SwimMixin:
    def swim(self):
        print("Swimming...")

class FlyMixin:
    def fly(self):
        print("Flying...")

# Eine Technik bei der Mehrfachvererbung genutzt wird
class Animal:
    def __init__(self, name):
        self.name = name
    def hello(self):
        print("I am", self.name)

class Dog(Animal, WalkMixin, SwimMixin):
    pass

class Bird(Animal, WalkMixin, FlyMixin):
    pass

class Fish(Animal, SwimMixin):
    pass

dog = Dog("Lilly")
dog.walk()   # Output: Walking...
dog.swim()   # Output: Swimming...
dog.hello()

bird = Bird("Birdie")
bird.walk()  # Output: Walking...
bird.fly()   # Output: Flying...
bird.hello()

fish = Fish("Nemo")
fish.swim()  # Output: Swimming...
fish.hello()
