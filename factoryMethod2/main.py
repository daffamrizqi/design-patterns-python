"""
The main goal of abc class is to provide a standardized way to test whether an object adheres 
to a given specification. It can also PREVENT any ATTEMPT TO INSTANTIATE a subclass that
doesn't ovveride a particular method in the superclass. And using abc, a class can derive 
identity from another class without any object inheritance
"""
import abc

# this class cannot be instantiated


class IPerson(metaclass=abc.ABCMeta):

    @abc.abstractmethod
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


# try to instantiate subclasses student and teacher
"""
We can instantiate Student and Teacher class because both of them is concrete subclasses of IPerson
abstract base class that implement the person_method. Because the Student and Teacher provide
an implementation for the person_method(), they are not abstract method, therefore can be
instantiated

"""
stu1 = Student()
stu1.person_method()
print(f"\nHi im student 1 and my name is: {stu1.name}")

teach1 = Teacher()
teach1.person_method()
print(f"\nHi im teacher 1 and my name is: {teach1.name}")


"""
A factory class which build Person object based on the input
"""


class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "student":
            return Student()
        if person_type == "teacher":
            return Teacher()
        raise Exception("Invalid Type!")


if __name__ == "__main__":
    choice = input("\nwhat type of person you want to create?\n")
    person = PersonFactory.build_person(choice.lower())
    person.person_method()
