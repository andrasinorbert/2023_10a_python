import sys
import os

if len(sys.argv)<2:
    print("Nem adtál meg fájlnevet!")
    print("Helyes használat: py {sys.argv[0]} fájlnév")
elif not os.path.exists(sys.argv[1]):
    print("Rossz fájlnevet adtál meg!")
else:
    filename= sys.argv[1]
    f=open(filename, encoding="utf-8")
    sorok=f.readlines()
    f.close()

    for i in range(len(sorok)):
        print(sorok[i].strip())