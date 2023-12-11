# Adatok:
#   Fájlban:    Dolgozók nevei szerepelnek
#               Mellette hogy havonta mennyi palacsintát sütöttek meg

# 1) Olvasd be a fájlt megfelelő adatszerkezetbe!

filename="input.txt"

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
