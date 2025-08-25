li=[1,2,3,4,5,6,7,8,8,9,10,8,9,1,4,3,5,6,6,10]
a=int(input("Enter a number you want to check: "))
count = 0
for i in li:
    if i == int(a):
        count += 1

print("The number", a, "is present in the list", count, "times.")
