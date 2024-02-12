import file_fvk as file

sorok=file.beolvas("input4")
print(sorok)

szamok=file.stringSzetszedoToIntList(
    sorok[1], 
    elejerol_ennyi_nem_kell=1, 
    vegerol_ennyi_nem_kell=1)
print(szamok)