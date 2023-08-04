class A:
    def __init__(self):
        print("in A Init")

    def m1(self):
        print("m1() in A")


class B:
    def __init__(self):
        super().__init__()
        print("in B Init")

    def m1(self):
        print("m1() in B")


class C(A, B):
    def __init__(self):
        super(C, self).__init__()
        print("in C Init")

    def m1(self):
        print("m1() in C")


# a = A()
# b = B()
c = C()
c.m1()
