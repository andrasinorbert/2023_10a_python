def fejlec(cim):
    szelesseg=30
    csillagok= "*"*szelesseg
    kozepso_csillag= "*"*int((szelesseg-len(cim))/2)
    print(csillagok)
    print(kozepso_csillag+cim+kozepso_csillag)
    print(csillagok)
#program_neve = "Programcíme"
#fejlec(program_neve)
#
#teszt=""
#for i in range(2,20):
#    teszt+="C"
#    fejlec(teszt)

x=11_123_321 # 11123321
print(x+1)

print(0o123)#8as számrendszer
print(0xABBA)#16os számrendszer
print(0b11000000) # 2es számrendszer

x=int("345",36) # tetszőleges számrendszerből váltás 10-esbe
print(x)

x=oct(321) # váltás 8-as szr-be
print(x)

x= hex(40096) # váltás 16-os szr-be
print(x)

x=bin(168) # váltás 2-es szr-be
print(x)

print(1/100000000) # 1e-08


str= 'Anya azt mondta hogy: "Érj haza időben!"'
print(str)
str= "Anya azt mondta hogy: \"Érj haza időben!\""

x= 6/4  # 1.5
y= 6//4 # 1 = int(1.5)
y= 6//-4 # -2
print(int(6//-4))
z= 6%4  # 2
zs = 2**5 # 32

print(9 % 6 % 2) # 1

a= 5
A =6
print(a) # 5
print(A) # 6

def abba():
    print("dgjdgj")

abba=60
print(abba())