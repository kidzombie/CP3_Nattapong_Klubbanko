try:
    input1 = int(input("A :"))
    input2 = int(input("B :"))
    print(input1/input2)
except ZeroDivisionError:
    print("O!!! Error")
except ValueError:
    print("Please input number instead string")
except:
    print("Something Error")