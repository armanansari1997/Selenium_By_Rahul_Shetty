
class Methods:
    def __init__(self):
        print("Constructor gets called")

    def m1(self):
        print("Instance Method")

    @classmethod
    def m2(cls):
        print("Class Method")

    @staticmethod
    def m3():
        print("Static Method")


method = Methods()
method.m1()
Methods.m2()
Methods.m3()