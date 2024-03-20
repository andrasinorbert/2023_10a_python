import sys
import os

def filebolLista(filename:str) -> list[str]:
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()
    return sorok

def sorokFeldolgoz(sorLista:list, elvalasztoKarakter:str=" ", fejlecVan:bool=False)-> tuple[list,list]:
    nevek=[]
    szamok=[]
    kezdosor=0
    if fejlecVan:
        kezdosor=1
    for i in range(kezdosor,len(sorLista)):
        egysor=sorLista[i].strip()
        egysorLista=egysor.split(elvalasztoKarakter)
        nevek.append(egysorLista[0])
        tmp=[]
        for j in range(1, len(egysorLista)):
            tmp.append(int(egysorLista[j]))
        szamok.append(tmp)
    return (nevek, szamok)

if len(sys.argv)<2:
    print("Nem adtál meg fájlnevet!")
    print("Helyes használat: py {sys.argv[0]} fájlnév")
elif not os.path.exists(sys.argv[1]):
    print("Rossz fájlnevet adtál meg!")
else:
    filename= sys.argv[1]
    sorok=filebolLista(filename)

    nevek, szamok=sorokFeldolgoz(sorok, ";", True)

    for i in range(len(nevek)):
        print(f"{nevek[i]}: {szamok[i]}")