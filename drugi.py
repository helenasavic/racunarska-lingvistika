devojka_iz_petnice = "Da je ljubav nauka\ndobio bih Nobela\nA da je ljubav knjiga\nuzeo bih NIN-a\n\nDevojke iz Petnice\nredom su pametnice\nA jedna među njima\nsad moje srce ima\n\nŽelim da sam projekat\ni da sam joj u mislima\nmrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima\n\nDevojka iz Petnice\nona meni znači sve\ni kada me se seti\nja hoću da poletim\n\nDevojka iz Petnice\nu koju sam zaljubljen\nsad uči tamo negde\nDa li pamti mene?\n\nHoću da sam tema\nU nečemu što sprema\nMrtvi Vizantinac\niz srednjeg veka pisac\nželim da sam bitan\nu njenim poslovima﻿"
mala_slova=devojka_iz_petnice.lower()
x=mala_slova.split("\n")
y=[]
for i in x:
    m=i.split(' ')
    for f in m:
        y.append(f)


neponovljene=[]
for rec in y:
    if rec not in neponovljene:
        neponovljene.append(rec)

neponovljene.sort()
d={}
for r in neponovljene:
    fr=0
    for s in y:
        if r==s:
            fr=fr+1
    d[r]=fr
for k, v in d.items():
    print(k, v)


    

