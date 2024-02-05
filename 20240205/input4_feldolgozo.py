import file_fvk as file

sorok=file.beolvas("input4")
print(sorok)

egysor=sorok[0].split(" ")
print(egysor)
szamok=file.strListToIntList(egysor)
print(szamok)