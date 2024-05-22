liste = [1,2,3,1,1,2,2,6,7,8,1,9,14,6,54,48,2]
tekrarEtmeyenler= []

for i in liste:
    if ( i not in bosListe):
        bosListe.append(i)
print(bosListe)