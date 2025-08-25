list1 = [20, 35, 45, 78]
list2 = [100, 200, 300, 400]

for a, b in zip(list1, reversed(list2)):
    print(a, b)