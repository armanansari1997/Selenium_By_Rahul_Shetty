class VariablesDemo:
    school = 'Telusko'

    def add(self, a, b):
        res = a + b
        return res


obj = VariablesDemo()
VariablesDemo.school = 'BBIT'
print(obj.add(10, 20), VariablesDemo.school)
