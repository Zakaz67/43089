numbers = [12, 5, 18, 7, 22, 14, 3, 30, 16, 9]
sa = 0
for i in numbers:
    if i > 15 and i % 2 == 0:
        sa = sa + i
        print(i)
print(sa)
