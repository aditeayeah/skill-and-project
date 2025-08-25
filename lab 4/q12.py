numbers = [12, 45, 23, 67, 34, 89, 5]

if len(numbers) < 2:
    print("List must have at least two numbers.")
else:
    unique_numbers = list(set(numbers))
    unique_numbers.sort(reverse=True)
    print("Second largest number:", unique_numbers[1])