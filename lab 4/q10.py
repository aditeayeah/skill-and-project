list1 = ["M", "na", "i", "Adi"]
list2 = ["y", "me", "s", "tya"]

result = [a + b for a, b in zip(list1, list2)]
print(result)