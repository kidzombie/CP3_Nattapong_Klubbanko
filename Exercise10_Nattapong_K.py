number = int(input("Input Number :"))
space = " "
remark = "*"
for i in range(number):
    j = i
    i = i*2+1
    print(space*(number-j) + remark*i + (space*(number-j)))
