# Feladat: feltétel szerinti adatbekérés

intervallum_min=3
intervallum_max=15
"""
x=input(f"Adj meg egy értéket [{intervallum_min}..{intervallum_max}]: ")
x= int(x)
if x>intervallum_min and x<intervallum_max:
    print("Jó számot adtál meg!")
else:
    print("Nem jó számot adtál meg!")
"""

feltetel=False
while not feltetel:
    x=input(f"Adj meg egy értéket [{intervallum_min}..{intervallum_max}]: ")
    x=int(x)
    if x>=intervallum_min and x<=intervallum_max:
        feltetel=True
    else:
        print("nem jót adtál meg!")

oszlopnevek=["első", "második"]
listak=[]
for listaszama in range(x):
    lista=[]
    for elem in oszlopnevek:
        ert=int(input(f"Add meg az értéket ({listaszama+1}.lista {elem}): "))
        lista.append(ert)
    print(lista)
    listak.append(lista)
print(listak)

listak_str=[]
for i in range(len(listak)):
    lista=[]
    for j in range(len(listak[i])):
        lista.append(str(listak[i][j]))
    listak_str.append(lista)

for lista_szamlalo in range(len(listak_str)):
    tamadasok=" ".join(listak_str[lista_szamlalo])
    print(f"{lista_szamlalo}.lista: {tamadasok}")

for lista_szamlalo in range(len(listak)):
    str_=str(lista_szamlalo+1)+". lista: "
    for elem_szamlalo in range(len(listak[lista_szamlalo])):
        str_+=str(listak[lista_szamlalo][elem_szamlalo])+" "
    print(str_)

