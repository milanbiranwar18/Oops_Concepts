# class Encap:
#     def getvalue(self, x):
#         self.a =x
#
#     def fun(self):
#         print(self.a)


class Encapsulation:
    """
    Program for implementing encapsulation using access modifier
    """

    def __init__(self):
        self._value1 = 100  # Protected
        self.__value2 = 200  # private

    def dispay(self):
        print(self._value1)
        print(self.__value2)


class Sub(Encapsulation):
    """
    Program for implementing encapsulation using access modifier in derived class
    """

    def show(self):
        print(self._value1)
        print(self.__value2)


if __name__ == '__main__':
    # obj = Encap()
    # obj.getvalue(100)
    # obj.fun()

    # obj1 = Sub()
    # obj1.show()

    obj2 = Encapsulation()
    obj2.dispay()
