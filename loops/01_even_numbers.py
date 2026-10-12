numbers = [12, 5, 8, 21, 6, 17, 4, 30]
sa = 0
for i in numbers:
    if i % 2 == 0:
        sa = sa + i
        print(i)
