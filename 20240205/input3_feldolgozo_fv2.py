import file_fvk

sorok=file_fvk.beolvas("input3")
print(sorok)
szamok=file_fvk.strListToIntList(sorok, 1, 1)
print(szamok)


# átnevezéssel
import file_fvk as file

sorok=file.beolvas("input3")
print(sorok)
szamok=file.strListToIntList(sorok, 1, 1)
print(szamok)