def f(x:int,y:int)->int:
    """
        f(x,y)=3x+2y
    """
    return 3*x+2*y

print(f(2,3))

print(f(3,2))

f(y=8, x=7)

print("ffhksehrfkh", end="")


x=print("szia")
print(x)

if( print("valami")==None):
    print("None-nal tért vissza")

def ki(x:any)->None:
    print(x)
    return

x=ki("géza")
if x==None:
    print("Nem volt visszatérési érték")

import math as m
def masodfoku(a:float,b:float,c:float):
    """
    Másodfokú megoldóképlet.
    return -1: a = 0
    return -2: diszkrimináns <0
    return int: 1 zérushely
    return tuple: 2 zérushely
    """
    if a==0:
        return -1
    d=b**2-4*a*c
    if d<0:
        return -2
    
    if d==0:
        return (-b )/ (2*a)
    
    x1=(-b+ m.sqrt(d) )/ (2*a)
    x2=(-b- m.sqrt(d) )/ (2*a)

    return x1,x2

x=masodfoku(0,3,1)
if x==-1:
    print("Az a érték 0 volt")
if x==-2:
    print("A diszkrimináns kisebb, mint 0")
if type(x)==type(tuple()):
    print("2 zérushelyünk van")
if type(x)==type(int()):
    print("1 zérushelyünk van")

# Ez igy nem jó megoldás, mert a zérushelyünk lehet -1, és -2 is akár, tehát így nem adunk vissza hiba értéket!

class A_NULLA(Exception):
    pass
class DISZKRIMINANS_KISEBB_NULLÁNÁL(Exception):
    pass

def masodfoku_hibadobassal(a:float,b:float,c:float):
    """
    Másodfokú megoldóképlet.
    ha a = 0: A_NULLA hiba
    ha a diszkrimináns <0: DISZKRIMINANS_KISEBB_NULLÁNÁL hiba
    return int: 1 zérushely
    return tuple: 2 zérushely
    """
    if a==0:
        raise A_NULLA
    d=b**2-4*a*c
    if d<0:
        raise DISZKRIMINANS_KISEBB_NULLÁNÁL
    
    if d==0:
        return (-b )/ (2*a)
    
    x1=(-b+ m.sqrt(d) )/ (2*a)
    x2=(-b- m.sqrt(d) )/ (2*a)

    return x1,x2

try:
    x=masodfoku_hibadobassal(0,1,2)
    if type(x)==type(tuple()):
        print("2 zérushelyünk van")
    if type(x)==type(int()):
        print("1 zérushelyünk van")
except A_NULLA:
    print("Az 'a' értéke 0")
except DISZKRIMINANS_KISEBB_NULLÁNÁL:
    print("A diszkrimináns kisebb nullánál")

def osszegzes_tetel(l:list)->int:
    """
    Összegzés prog tétel
    return elemek összege
    """
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s

print(osszegzes_tetel([2,3,4]))