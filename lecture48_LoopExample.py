number = int(input())
text =""
for i in range(number):
    text = text + "*"
    print(text)


number1 = int(input())
for x in range(number1):
    text1 = ""
    for y in range(x+1):
        text1 += "*"
    print(text1)

number2 = int(input())
for z in range(number2):
    print("*"*(z+1))