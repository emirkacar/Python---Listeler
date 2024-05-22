#Tekrar eden sayilari bos bir diziye atan algoritmas
liste = [1,2,3,4,5,1,2,1,6]
ciftElemanlar = []

for i in liste:
    if((liste.count(i) > 1) and (i not in ciftElemanlar)):
        ciftElemanlar.append(i)
print(ciftElemanlar)



#Ortalama bulma algoritmasi

liste = [1,2,3,4,5,6]
toplam=0

for i in liste:
    toplam+=i

print("Ortalama = %.2f" %(toplam/len(liste)))


#Listenin tersini alma algoritmasi 1.Yol

liste=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(liste),0,-1):
    print(i,end=" ")


#Listenin tersini alma algoritmasi 2.Yol

liste=[1,2,3,4,5,6,7,8,9,10]

liste.reverse()
print(liste)


#Listenin tersini alma algoritmasi 3.Yol

liste=[1,2,3,4,5,6,7,8,9,10]
listeninTersi=[]
for i in liste:
    listeninTersi.insert(0,i)
print(listeninTersi)








