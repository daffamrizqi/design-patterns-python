from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    """
    The creator class declares the factory method that is supposed to return an object
    of a Product class. The creator's subclasses usually provide the implementation
    of this method
    """

    @abstractmethod
    def factory_method(self):
        """
        Note that the creator may also provide some default implementation of the 
        factory method
        """
        pass