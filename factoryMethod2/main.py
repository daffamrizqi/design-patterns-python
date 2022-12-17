"""
The main goal of abc class is to provide a standardized way to test whether an object adheres 
to a given specification. It can also PREVENT any ATTEMPT TO INSTANTIATE a subclass that
doesn't ovveride a particular method in the superclass. And using abc, a class can derive 
identity from another class without any object inheritance
"""
from abc import ABCMeta,  abstractstaticmethod

# this class cannot be instantiated


class IPerson(metaclass=ABCMeta):

    @abstractstaticmethod
    def person_method():
        """Interface method"""
        pass


class Student(IPerson):
    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")


class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic teacher name"

    def person_method(self):
        print("I am a teacher")


"""
A factory class which build Person object based on the input
"""


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        raise Exception("Invalid Type!")


if __name__ == "__main__":
    choice = input("what type of person you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()
