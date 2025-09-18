"""
Demonstrate polymorphism by creating:

    A base class Animal with method move()
    Three derived classes: Fish, Bird, Dog with different implementations of move()
        fish swims, bird flies, dog runs
    A function that takes any animal and calls its move() method
"""
class Animal:
    def move(self):
        print("The animal moves in some way.")
class Fish(Animal):
    def move(self):
        print("The fish swims in the water.")

class Bird(Animal):
    def move(self):
        print("The bird flies in the sky.")

class Dog(Animal):
    def move(self):
        print("The dog runs on the ground.")
def make_animal_move(animal):
    animal.move()
fish = Fish()
bird = Bird()
dog = Dog()

make_animal_move(fish)
make_animal_move(bird)
make_animal_move(dog)
