s = input("enter your word:")
result = ""

for ch in s:
    if ch not in result:
        result += ch

print("words without duplicate:", result)