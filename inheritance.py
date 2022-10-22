# Single Inheritance
class Sample1:  # super class/ base class/ parent class
    """
    Program for base/parent class for single inheritance
    """

    def fun1(self):
        print("Class - Sample1")


class Sample2(Sample1):  # child class / sub class/ derived class
    """
    Program for derived class for single inheritance
    """

    def fun2(self):
        print("Class - Sample2")


# Multilevel Inheritance
class Sample3:
    """
    Program for base/parent class for Multilevel inheritance
    """

    def fun3(self):
        print("Class - Sample3")


class Sample4(Sample3):
    """
    Program for derived class for Multilevel inheritance
    """

    def fun4(self):
        print("Class - Sample4")


class Sample5(Sample4):
    """
    Program for derived class for Multilevel inheritance
    """

    def fun5(self):
        print("Class - Sample5")


# Hierarchical Inheritance
class Sample6:
    """
    Program for base/parent class for Hierarchical inheritance
    """

    def fun6(self):
        print("Class - Sample6")


class Sample7(Sample6):
    """
    Program for derived class for Hierarchical inheritance
    """

    def fun7(self):
        print("Class - Sample7")


class Sample8(Sample6):
    """
     Program for derived class for Hierarchical inheritance
    """

    def fun8(self):
        print("Class - Sample8")


# Multiple Inheritance
class Sample9:
    """
     Program for parent class for Multiple inheritance
    """

    def fun9(self):
        print("Class - Sample9")


class Sample10:
    """
    Program for derived class for Multiple inheritance
    """

    def fun10(self):
        print("Class - Sample10")


class Sample11(Sample9, Sample10):
    """
    Program for derived class for Multiple inheritance
    """

    def fun11(self):
        print("Class - Sample11")


# Hybrid Inheritance
class Sample12:
    """
    Program for parent class for Hybrid inheritance
    """

    def fun12(self):
        print("Class - Sample12")


class Sample13(Sample12):
    """
    Program for derived class for Hybrid inheritance
    """

    def fun13(self):
        print("Class - Sample13")


class Sample14(Sample12):
    """
    Program for derived class for Hybrid inheritance
    """

    def fun14(self):
        print("Class - Sample14")


class Sample15(Sample13, Sample14):
    """
    Program for derived class for Hybrid inheritance
    """

    def fun15(self):
        print("Class - Sample15")


if __name__ == '__main__':
    obj = Sample2()
    obj.fun2()  # calling Sample2 class method
    obj.fun1()  # calling Sample1 class method
    print("-----------------------------------------------------")

    ob = Sample5()
    ob.fun5()
    ob.fun4()
    ob.fun3()
    print("--------------------------------------------------")

    obj1 = Sample8()
    obj1.fun8()
    obj1.fun6()

    obj2 = Sample7()
    obj2.fun7()
    obj2.fun6()
    print("----------------------------------------------------------------")

    obj3 = Sample11()
    obj3.fun11()
    obj3.fun10()
    obj3.fun9()
    print("--------------------------------------------------------------")

    obj4 = Sample15()
    obj4.fun15()
    obj4.fun14()
    obj4.fun12()
    obj4.fun13()
