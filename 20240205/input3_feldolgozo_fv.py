
def beolvas(filename):
    file= open(filename)
    sorok= file.readlines()
    file.close()
    return sorok

def feldolgoz(sorok, elsosor=0, a_vegerol_ennyi_sor_nem_kell=0):
    szamok=[]
    for i in range(elsosor,len(sorok)-a_vegerol_ennyi_sor_nem_kell):
        szamok.append(int(sorok[i].strip()))
    return szamok

sorok=beolvas("input3")
print(sorok)
szamok=feldolgoz(sorok, 1, 1)
print(szamok)