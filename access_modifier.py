# For public
class Sample1:
    """
    Program for public access modifiers
    """

    def access_samp1(self):
        print('World')


class Sample2:
    """
    Program for implementing public access modifiers
    """

    def access_samp2(self):
        print("Hello")
        obj = Sample1()
        obj.access_samp1()


obj1 = Sample2()
obj1.access_samp2()

print("---------------------------------------------------")


# for protected
class Sample3:
    """
    Program for protected access modifiers
    """

    def _access_samp3(
            self):  # For protected access modifier we use one underscore like _xyz and it can implement by inheriting only
        print("World")


class Sample4(Sample3):
    """
    Program for implementing protected access modifiers
    """

    def access_samp4(self):
        print("Hello")
        obj2 = Sample3()
        obj2._access_samp3()


obj3 = Sample4()
obj3.access_samp4()

print("----------------------------------------------------------")


# For Private,  It can implement in same class only  using double underscore like __xyz
class Sample5:
    """
    Program for private access modifiers
    """

    def __access_samp5(self):
        print("World")

    def access_samp6(self):
        """
        Program for implementing private access modifiers
        :return: will return private class code
        """
        print("Hello")
        a = Sample5()
        a.__access_samp5()


obj4 = Sample5()
obj4.access_samp6()
