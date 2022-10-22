class MethodOverriding:
    """
    Program for parent class to override
    """

    def show(self):
        print("parent class method")

        # class OverridenClass(MethodOverriding):
        """
        Program for derived class to override
        """

        # pass


class OverridenClass(MethodOverriding):
    """
    Program for derived class to override
    """

    def show(self):
        print("derived class method")


if __name__ == '__main__':
    obj = OverridenClass()
    obj.show()
