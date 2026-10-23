renly = int(input("введи число пупсик: "))
kolichestvo = 0

while renly != 0:
    sa = renly
    renly = int(input("число:"))

    if renly == 0:
        break

    if renly > sa:
        kolichestvo += 1

print(kolichestvo)
