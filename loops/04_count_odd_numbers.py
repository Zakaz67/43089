numbers = [11, 4, 18, 7, 22, 5, 30, 13, 16]
sa = 0
for i in numbers:
    if i % 2 == 1:
        sa = sa + 1
        print(i)
print(sa)
