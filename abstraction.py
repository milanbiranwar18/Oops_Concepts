from abc import ABC, abstractmethod


# ABC - abstract base class

class Computer(ABC):  # abstract class
    """
    Program for Abstract class
    """

    @abstractmethod  # abstract method
    def process(self):
        """
        Program for Abstract method
        """
        pass


class Laptop(Computer):  # derived class
    """
    Program for derived class
    """

    def process(self):
        print("derived class")


if __name__ == '__main__':
    # lap = Laptop()
    # lap.process()
    obj = Computer()
    obj.process()
