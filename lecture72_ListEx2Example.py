menuList = []

def showBill():
    totalPrice = 0
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0])
        totalPrice += int(menuList[number][1])
    print("Total price :",totalPrice)
while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])


print(menuList)
showBill()

