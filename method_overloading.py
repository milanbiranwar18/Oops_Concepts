import logging

logging.basicConfig(filename="calculate_emp_wage.log",
                    filemode='a',
                    format='%(asctime)s %(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

class MethodOverloading:
    """
    Program for Method Overloading
    """
    try:
        def sum(self, a=None, b=None, c=None):

            s = 0

            if a != None and b != None and c != None:
                s = a + b + c

            elif a != None and b != None:
                s = a + b

            else:
                s = a
            return s

    except Exception as e:
        logging.error(e)


if __name__ == '__main__':
    obj = MethodOverloading()
    print(obj.sum(2, 3, 5))
