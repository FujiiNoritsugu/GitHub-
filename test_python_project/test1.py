from test2 import test2_fn
from test3.test3 import test3_fn
from test3.test4.test4 import test4_fn, test4_class
from test3.test4 import test4_obj2

def main():
    test2_fn()
    test3_fn()
    test4_fn()
    test4_obj = test4_class()
    test4_obj._print_a()
    test4_obj._print_b()
    test4_obj2._print_b()

if __name__ == '__main__':
    main()
