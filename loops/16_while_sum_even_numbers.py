stanis_baratheon = int(input("тут твое число :"))
sumka = 0
kolichestvo = 0

if stanis_baratheon % 2 == 0 and stanis_baratheon != 0:
        sumka += stanis_baratheon
        kolichestvo += 1

while stanis_baratheon != 0:
    stanis_baratheon = int(input("тут твое число :"))
    if stanis_baratheon % 2 == 0 and stanis_baratheon != 0:
        sumka += stanis_baratheon
        kolichestvo += 1
print(sumka)
print(kolichestvo)
