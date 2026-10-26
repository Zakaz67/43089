text = input("введи текст:").lower()
sa = 0

for letter in text:
    if letter in "aeiou":
        sa += 1

print(sa)
