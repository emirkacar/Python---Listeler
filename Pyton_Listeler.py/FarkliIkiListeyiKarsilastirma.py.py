#Farklı İki Listeyi Karşılaştırma:
liste1 = [1,2,3,4,5]
liste2 = [3,4,5,6,7]
ortakListe = []

for i in liste1:
    if i in liste2:
        ortakListe.append(i)
print(ortakListe)
    



