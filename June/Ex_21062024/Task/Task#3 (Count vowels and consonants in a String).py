input_str = str(input("Enter the name:"))
vowels = 0
consonants = 0
for i in input_str:
    if (
            i == 'a' or i == 'e' or i == 'i'
            or i == 'o' or i == 'u' or
            i == 'A' or i == 'E' or i == 'O' or
            i == "I" or i == 'U'):
        vowels = vowels+1
    else:
        consonants = consonants+1

print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
