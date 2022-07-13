Username = input("Username :")
Password = input("Password :")
if Username == "admin" and Password == "1234":
    print("----Welcome to FruitShop----")
    print("Banana = 10 THB/ea")
    print("Orange = 15 THB/ea")
    print("Papaya = 17 THB/ea")
    print("Mango  = 20 THB/ea")
    print("Grape  = 12 THB/ea")
    item = (input("Input :"))
    if item == "Banana" or item == "banana":
        BananaQuantity = int(input("quantity :"))
        print("Total Price =", BananaQuantity*12)
    elif item == "Orange" or item == "orange":
        OrangeQuantity = int(input("quantity :"))
        print("Total Price =", OrangeQuantity*15)
    elif item == "Papaya" or item == "papaya":
        PapayaQuantity = int(input("quantity :"))
        print("Total Price =", PapayaQuantity*17)
    elif item == "Mango" or item == "mango":
        MangoQuantity = int(input("quantity :"))
        print("Total Price =", MangoQuantity*20)
    elif item == "Grape" or item == "grape":
        GrapeQuantity = int(input("quantity :"))
        print("Total Price =", GrapeQuantity*12)
    else:
        print("Your item is not available")
else:
    print("User or Password not authorize")

