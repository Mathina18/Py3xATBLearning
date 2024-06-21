input_string = str(input("Enter the string:"))

cleaned_string = input_string.replace(" ", "").lower()
if cleaned_string == cleaned_string[::-1]:
    print(f"'{input_string}' is a palindrome")
else:
    print(f"'{input_string}' is not a palindrome")