tupleExample = ('Prame', 'First','Aces')
print(tupleExample)
tupleExample2 = ('Bank','Kay')
print(tupleExample2)
tupleExample3 = tupleExample + tupleExample2 *2
print(tupleExample3)
print(tupleExample3[0])
print(tupleExample3[2])
print(tupleExample3[:3])
print('Yeen' in tupleExample3)
print('First' in tupleExample3)
for i in tupleExample3:
    print("Hello", i)