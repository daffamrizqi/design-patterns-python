from __future__ import annotations
import abc


class Creator(abc.ABC):
    """
    The Creator class declares the factory method that is supposed to return
    an object of a Product class. The Creator's Subclasses usually provide the
    implementation of this method
    """

    @abc.abstractmethod
    def factory_method(self):
        """
        Note that the creator may also provide some defaults implementation
        of the factory method
        """
        pass

    def some_operation(self):
        """
        Also note that, depote its name, the Creator's primary responsibility
        is not CREATING PRODUCTS. Usually, it contains some core business logic
        that relies on Product Objects, returned by The factory method. Subclasses
        can indirectly change that business logic by overriding the facotry
        method and returning a different type of product from it
        """

        # call the factory method to create a Product object
        product = self.factory_method()

        # now use the product
        result = f"Creator: the same creator's code has just worked with {product.operation()}"
        return result


"""
Concrete creator s override the facotry method(which is an abstract method) in order to change the resulting
product's type
"""


class ConcreteCreator1(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This way the Creator
    can stay independent of conrete product classes
    """

    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(abc.ABC):
    """
    The product interface declares the operation that all concrete products
    must implement
    """

    @abc.abstractmethod
    def operation(self) -> str:
        pass


"""
Concrete products provide various implementations of the product interface
"""


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct1}"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "{Result of the ConcreteProduct2}"


def client_code(creator: Creator) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via the base
    interface, you can pass it any creator's subclass
    """
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("App: Lunched with the ConcreteProduct1")
    client_code(ConcreteCreator1())
    print("\n")

    print("App launched with the ConcreteCreator2")
    client_code(ConcreteCreator2())
    print("\n")
