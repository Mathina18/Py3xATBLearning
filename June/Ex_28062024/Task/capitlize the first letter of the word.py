input_text = str(input("Enter your string:"))

# Split the input text into words
words = input_text.split()

# Transform the words
words[0] = words[0].lower()
for i in range(1, len(words)):
    words[i] = words[i].capitalize()

# Join the transformed words back into a single string
output_text = ' '.join(words)

# Print the output
print(output_text)