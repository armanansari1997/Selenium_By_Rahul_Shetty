class ExceptionDemo:
    def division(self):
        num1 = int(input("Enter 1st number "))
        num2 = int(input("Enter 2nd number "))
        try:
            out = num1 / num2
            print(out)
            print("after result")
            print("after result")
        except ZeroDivisionError as e:
            print("Wrong input ", e)
        except Exception as e:
            print("Exception Occurred ", e)
        finally:
            print("System Closed")


obj = ExceptionDemo()
obj.division()


# Raise A Exception
a = 2
if a == 2:
    raise Exception("Input Match Exception")
else:
    print("Input MisMatch")
