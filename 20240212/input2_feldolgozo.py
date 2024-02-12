import file_fvk as file

sorok=file.beolvas("input2")
print(sorok)

szamok=file.stringSzetszedoToIntList(sorok[0], elejerol_ennyi_nem_kell=1)
print(szamok)