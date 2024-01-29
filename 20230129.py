

def osszegzes_osszeadassal(lista:list)->int:
    s=0
    for i in range(len(lista)):
        s=s+lista[i]
    return s

def osszegzes_szorzassal(lista:list)->int:
    s=1
    for i in range(len(lista)):
        s=s*lista[i]
    return s

def osszegzes(lista:list, func)->int:
    s=lista[0]
    for i in range(1,len(lista)):
        s=func(s,lista[i])
    return s

def osszead(num1:int, num2:int)->int:
    return num1+num2
def osszeszoroz(num1:int, num2:int)->int:
    return num1*num2
print(osszegzes([1,2,3,4,5], osszead))
print(osszegzes([1,2,3,4,5], osszeszoroz))
print(osszegzes([1,2,3,4,5], lambda num1,num2:num1+num2))
print(osszegzes([1,2,3,4,5], lambda num1,num2:num1*num2))

osszeadas= lambda num1, num2: num1+num2
print(osszegzes([1,2,3,4,5], osszeadas))


def megszamlalas(lista:list, condition:bool)->int:
    c=0
    for i in range(len(lista)):
        if condition(lista[i]):
            c+=1
    return c

def paros_e(num:int)->bool:
    return num%2==0

print(megszamlalas([1,2,3,4,5],paros_e))
print(megszamlalas([1,2,3,4,5],lambda num:num%2==0))

def szelsoertek_kivalsztas(lista:list, condition)->tuple:
    index=0
    ertek=lista[0]
    for i in range(1,len(lista)):
        if condition(lista[i], ertek):
            index=i
            ertek=lista[i]
    return index,ertek
def kisebb(num1, num2):
    return num1<num2
kisebb_lambda= lambda num1,num2: num1<num2
print(szelsoertek_kivalsztas([2,6,5,3,98,4,-2,5],kisebb))
print(szelsoertek_kivalsztas([2,6,5,3,98,4,-2,5],kisebb_lambda))
print(szelsoertek_kivalsztas([2,6,5,3,98,4,-2,5],lambda num1,num2: num1<num2))


osszeadas= lambda num1, num2: num1+num2

print(osszeadas(2,3))

banner=lambda szoveg:print(30*"*"+"\n"+
        ((30-len(szoveg))//2)*"*"+szoveg+((30-len(szoveg))//2)*"*"
        +"\n"+30*"*")

banner("Szia")
banner("Aha")

lista=[2,3,7,6,4,3,2,9]

Otnel_kiebb_e = lambda num: num<5

c=0
for i in range(len(lista)):
    if Otnel_kiebb_e(lista[i]):
        c+=1
print(c)