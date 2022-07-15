def vatCalculate(totalPrice):
    result = totalPrice + (totalPrice*7/100)
    return result

print(vatCalculate(100))

def vatCalculate1():
    totalPrice1 = int(input("Total price :"))
    result1 = totalPrice1 + (totalPrice1*7/100)
    return "Total price include vat :" + str(result1)

print(vatCalculate1())


