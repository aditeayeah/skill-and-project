input_string = input("Enter a string: ")

original_string_display = input_string
cleaned_string = input_string.lower()
reversed_string = cleaned_string[::-1]

print("Actual string:", original_string_display)
print("Reversed string:", reversed_string)

if cleaned_string == reversed_string:
    print("String is palindrome")
else:
    print("String is not palindrome")
