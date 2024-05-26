#List Comprehension kullanimi

liste = [3,4,5]
liste1 = [i*i for i in liste]
print(liste1)

liste2 = [ (1,2) , (3,4) , (5,6)]

liste3 = [i*j for i,j in liste2]
print(liste3)


liste = [(1, 2), (3, 4), (5, 6)]
yeniListe = []

for i in liste:
    carpim = 1
    for j in i:
        carpim *= j
    yeniListe.append((carpim,))

print(yeniListe)



liste = [ [1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]

listComp = [ i for l in liste for i in l ]

print(listComp)





