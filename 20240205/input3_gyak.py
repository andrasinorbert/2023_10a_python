import file_fvk as file

sorok=file.beolvas("input3")
szamok=file.strListToIntList(sorok,1,1)
print(szamok)

# 1. feladat: hány darab számunk van?
print(f"1.feladat: {len(szamok)} db szám van")

# 2. feladat: számok összege
s=0
for i in range(len(szamok)):
    s+= szamok[i]
print(f"2.feladat: szamok összege: {s}")

# 3. feladat: számok szorzata
s=1
for i in range(len(szamok)):
    s*= szamok[i]
print(f"3.feladat: szamok szorzata: {s}")

# 4. feladat: legnagyobb szám
max=szamok[0]
for i in range(1, len(szamok)):
    if max<szamok[i]:
        max=szamok[i]
print(f"4. feladat: legnagyobb szám: {max}")

# 5. feladat: 3. szám értéke
print(f"5. feladat: 3.szám értéke: {szamok[2]}")

# 6. feladat: páratlan számok közül a legkisebb
min=1000000
for i in range(len(szamok)):
    #if szamok[i]%2==1 and szamok[i]<min:
    if szamok[i]%2==1:
        if szamok[i]<min:
            min=szamok[i]
print(f"6. feladat: legkisebb ptlan szám: {min}")
