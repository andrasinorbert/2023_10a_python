file= open("input2")
sorok= file.readlines()
file.close()

print(sorok)

szamok=[]
for i in range(1,len(sorok)-1):
    szamok.append(int(sorok[i].strip()))
print(szamok)