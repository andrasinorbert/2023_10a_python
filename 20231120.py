
#x=input("x=")
#input("y=")

x="ha"*3
print(x)

x= 3 ==2
print(x)

x= 3 !=2
print(x)

x=2
if x==3:
    print("Az x értéke: 3")
else:
    print("Az x értéke nem 3")


x=5
if x==3:
    print("Az x értéke: 3")
elif x<3:
    print("Az x értéke kisebb, mint 3")
else:
    print("egyik feltétel sem igaz")

# ide
x=5
feltetel= True
while feltetel:
    print("ciklusmag")
    if(x==7):
        feltetel=False
    x+=1
print(x)

i=1
while not True:
    print("Szeretem a Puskást!", i)
    i+=1

while not True:
    pass

for i in range(10):
    pass # 0 -9

for i in range(2,5):
    pass # 2,3,4

for i in range(2,10,3):
    pass # 3,5,8

# break
# continue

x = "szia"
for i in x:
    print(i)

x=5
while x<4:
    pass
else:
    print("nem lépett a ciklusba")

ijk=7
for ijk in range(12,10):
    print(ijk)
else:
    print("else ág:", ijk)

x=3
y=6
print(x>y)
print(not(x>y))
print(not(x<=y))

print(True and True)
print(True and False)
print(True and False and True)
print(True or False or True)
print(True or False or False)

print( 1 and 0)
print(1 and 1)

print( (1 and 1) and (1 and 1))
print( (1 and 1) and (1 and 0))
print( (1 or 1) or (1 or 1))
print( (1 or 1) or (1 or 0))
print( (1 or 0) or (1 or 0))
print( (1 or 0) or (0 or 0))
print( (0 or 0) or (0 or 0))

a,b,c,d=1,1,1,1
print( (a or b) and (c or d))
print( (a and b) or (c and d))

# XOR
print( 1 ^ 0)
print( 1 ^ 1)

print( 1 & 1)
print( 3 & 2)
# 3: 11
# 2: 10
# eredmény: 10
print( 3 | 2)
# 3: 11
# 2: 10
# eredmény: 11

print( ~5)
#  5: 101
# ~5: 010
