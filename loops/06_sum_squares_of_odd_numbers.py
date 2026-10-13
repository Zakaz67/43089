numbers = [3, 8, 11, 4, 7, 12, 5]
sa = 0
for i in numbers:
    if i % 2 == 1:
        sa = sa + i**2
        print(i**2)
print(sa)
