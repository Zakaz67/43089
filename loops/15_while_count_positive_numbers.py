mika = int(input("введи число пацик:"))
andao = 0
miku = 0

andao += mika
if andao > 0:
    miku += 1

while mika != 0:
    mika = int(input("введи число пацик:"))
    if mika > 0:
        miku += 1
print(miku)
