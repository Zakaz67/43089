duca = int(input("Введи число ниже паря:"))
sa = 0
anzo = 0

if duca != 0:
    sa += duca
    anzo += 1

while duca != 0:
    duca = int(input("число плиз:"))
    if duca == 0:
        break
    sa += duca
    anzo += 1

print(sa)
print(anzo)
