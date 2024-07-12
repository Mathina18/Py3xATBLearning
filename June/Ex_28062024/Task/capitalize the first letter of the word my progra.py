text = str(input("Enter your text:"))
words = text.split()

result = []
for word in words:
    if word[0].isupper():
        result.append(word[0].lower() + word[1:])
    else:
        result.append(word[0].upper() + word[1:])

output_text = ' '.join(result)
print(output_text)





