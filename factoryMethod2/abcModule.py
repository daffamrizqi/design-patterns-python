import abc


class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self):
        self.name = "Cat"
        print("HI I'm a fucking cat not a pussy!")

    def make_sound(self):
        print("Hi I'm a cat, meow")


class Dog(Animal):
    def __init__(self):
        self.name = "dog"
        print("yea im a dog, got problem?")

    def make_sound(self):
        print("Hi I'm a dog, Woof")


# instance of Cat and Dog classes
cat1 = Cat()
cat1.make_sound()

dog1 = Dog()
dog1.make_sound()


# make factory method to define what animal type based on input
class AnimalFactory:
    # staticmethod E below
    @staticmethod
    def decide_animal(animal):
        if animal == "cat":
            print("You chose CAT in the fckin factory!")
            return Cat()
        if animal == "dog":
            print("you chose DOG in the fckin factory!")
            return Dog()
        raise Exception("Invalid type of animal!")


if __name__ == "__main__":
    choice = input("Choose cat or dog Bitchis!:\n")
    animal = AnimalFactory.decide_animal(choice.lower())
    animal.make_sound()

"""
The Animal class is an abstract base class that defines an abstract method called make_sound()
The Dog and Cat classes are CONCRETE SUBCLASSES of Animal abstract base class that implement
the make_sound method. Because the Dog and Cat classes provide an implementation for the 
make_sound() method, they are not abstract method. Therefore, they can be instantiated
"""


# @staticmethod
class MyClass:
    @staticmethod
    def my_static_method():
        # code goes here
        pass


""" You can then call the staticmethod on the class itself, or on any instance of the class """
MyClass.my_static_method()

obj = MyClass()
obj.my_static_method()

# staticmethod example


class MyCalculator:
    @staticmethod
    def average(numbers):
        return sum(numbers) / len(numbers)


nums = [1, 2, 3]
print(f"\nAverage of {nums}: {MyCalculator.average(nums)}")

"""
Note that static methods do not have access to the instance variables or instance methods
of the class. They can only access class variables and other static methods
"""
