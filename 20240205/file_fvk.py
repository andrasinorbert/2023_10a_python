def beolvas(filename:str)->list[str]:
    """
    1. Egy fájlt megnyit
    2. sorait beleteszi egy listába
    3. bezárja a fájlt
    Return: lista
    """
    file= open(filename)
    sorok= file.readlines()
    file.close()
    return sorok

def strListToIntList(sorok:list[str], elsosor:int=0, a_vegerol_ennyi_sor_nem_kell:int=0)->list[int]:
    """
    1 elem:
    - leveszi a felesleget
    - integerré alakitja
    """
    szamok=[]
    for i in range(elsosor,len(sorok)-a_vegerol_ennyi_sor_nem_kell):
        szamok.append(int(sorok[i].strip()))
    return szamok

def stringSzetszedoToIntList(szoveg:str, separator=" "):
    egysor=szoveg.split(separator)
    szamok=strListToIntList(egysor)
    return szamok