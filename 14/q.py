class A:
    def __init__(self, a):
        self.a = a

    def get_attrs(self):
        return self.a


class B(A):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

    def get_attrs(self):
        fisrst_attr = super().get_attrs()
        return fisrst_attr, self.b


class C(B):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def get_attrs(self):
        fisrst_2_attr = super().get_attrs()
        return fisrst_2_attr, self.c


import contextlib


class my_man:
    def __enter__(self):
        print('jnjds')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('jjj')
