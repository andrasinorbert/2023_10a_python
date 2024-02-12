import file_fvk as file

sorok=file.beolvas("input5")
print(sorok[1])

szamok=file.stringSzetszedoToIntList(
    sorok[1], 
    elejerol_ennyi_nem_kell=1, 
    vegerol_ennyi_nem_kell=1,
    adatseparator=";")
print(szamok)