def fileToString(filename:str)->str:
    file= open(filename)
    sor= file.readline()
    file.close()
    return sor

def feldolgozo(
        beolvasottSor:str,
        elvalasztoKarakter:str=" ",
        adatokKezdete:int=0,
        adatokVege:int=0)->list[int]:
    sor=beolvasottSor.strip()
    sor_lista_str=sor.split(elvalasztoKarakter)
    szamok=[]
    for i in range(adatokKezdete,len(sor_lista_str)-adatokVege):
        szamok.append(int(sor_lista_str[i]))
    return szamok

print(feldolgozo(fileToString("input1")))
print(feldolgozo(
    beolvasottSor=fileToString("input2"),
    elvalasztoKarakter=" ",
    adatokKezdete=2,
    adatokVege=2))
print(feldolgozo(
    beolvasottSor=fileToString("input3"),
    elvalasztoKarakter=",",
    adatokKezdete=1,
    adatokVege=1))