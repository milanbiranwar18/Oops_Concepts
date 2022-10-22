class Sample1:
    """
    Function for operator overriding using special method
    """

    def __init__(self, x):
        self.x = x

    def __add__(self, other):  # special method
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x


class Sample2:
    """
     Function for operator overriding using special method
    """

    def __init__(self, x):
        self.x = x

    def __sub__(self, other):
        return self.x - other.x


if __name__ == '__main__':
    obj1 = Sample1(10)
    obj2 = Sample1(20)
    print(obj1 + obj2)
    print(obj1 - obj2)
    print(obj1 * obj2)

    obj1 = Sample2(20)
    obj2 = Sample2(10)
    print(obj1 - obj2)
