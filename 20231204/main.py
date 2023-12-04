
fajlnev="2023_10a_python/20231204/input.txt"
f=open(fajlnev, "r") # read
sorok=f.readlines()
f.close()

for i in range(len(sorok)):
    sorok[i]=sorok[i].strip()
print(sorok[0])

sum=int(sorok[1])+int(sorok[2])
print(sum)