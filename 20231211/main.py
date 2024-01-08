# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename="./input.txt"

file=open(filename, "r")
file_lista=file.readlines()
file.close()

name_list=[]
pancake_list=[]
for i in range(len(file_lista)):
    _lista=file_lista[i].strip()
    _lista_parts=_lista.split()

    # így is lehet: _lista_parts=file_lista[i].strip().split()
    name_list.append(_lista_parts[0])

    _l=[]
    for j in range(1,len(_lista_parts)):
        _l.append(int(_lista_parts[j]))
    pancake_list.append(_l)

# print(name_list)
# print(pancake_list)
# for i in range(len(pancake_list)):
#     print(len(pancake_list[i]))

# 2) írd ki az adatokat szépen(!!) az alábbbi fejléccel:
#       "Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
fejlec="Név\tJanuary\tFebruary\tMarch\tApril\tMay\tJune\tJuly\tAugust\tSeptember\tOctober\tNovember\tDecember"
print(fejlec)
for i in range(len(name_list)):
    print(name_list[i], end="\t")
    for j in range(len(pancake_list[i])):
        print(pancake_list[i][j], end="\t")
        if j==1 or j==8 or j==10: print("",end="\t")
    print()


# 3) Add meg, hogy márciusban ki sütötte a legtöbb palacsintát!
month_index=3-1
max_ert=pancake_list[month_index][0]
max_index=0
for i in range(1,len(pancake_list)):
    if max_ert<pancake_list[i][month_index]:
        max_ert=pancake_list[i][month_index]
        max_index=i

print(f"A legtöbb palacsintát márciusban {name_list[i]} sütötte")

# 4) Add meg, hogy ki sütötte az évben a legkevesebb palacsintát!

min_ert= -1
min_index=-1
for i in range(len(pancake_list)):
    palacsintak_szama=0
    for j in range(len(pancake_list[i])):
        palacsintak_szama+=pancake_list[i][j]
    #print(f"{i} {palacsintak_szama}")
    if palacsintak_szama<min_ert or min_index==-1:
        min_ert=palacsintak_szama
        min_index=i
    #print(f"min: {min_index} {min_ert}")

print(f"A legkevesebb palacsintát {name_list[min_index]} sütötte az évben.")

# 5) Add meg, hogy az a személy, akinek B-vel kezdődik a neve, Májusban hány palacsintát sütött.
month_index=5-1
for i in range(len(name_list)):
    if name_list[i][0] == "B":
        print(f"{name_list[i]} májusban {pancake_list[i][month_index]} palacsintát sütött")

# 6) Volt-e olyan személy, akinek az évben változó teljesítménye volt?
#       Pl: sütött valamennyit, majd a következő hónapban többet, a következőben az előzőnél kevesebbet stb
#       írd ki a személy nevét!

x=1 if False else 2 if True

"""
for i in range(len(pancake_list)):
    j=0
    # -1, ha palacsinta[month-1]<palacsinta[month]
    # 0, palacsinta[month-1]=palacsinta[month]
    # 1, ha palacsinta[month-1]>palacsinta[month]
    last_res=-1 if pancake_list[i][0]<pancake
    curr_res=None
    while 
"""