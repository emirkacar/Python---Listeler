#Append() fonksiyonu kullanmadan listeye eleman ekleme ardindan remove kullanmadan silme,daha sonra reverse() kullanmadan tersini almalgoritmasi
#Eleman ekleme
liste = []
i = 0

while i < 7:
  x = int(input("Lütfen bir sayi giriniz: "))
  liste = liste + [x]  # Elemani listeye eklemek için '+' operatörünü kullanin
  i += 1

print(liste)

#Elemen Silme
liste1=[1,2,3,4,45,60,70,90]

silinecekEleman=4
yeniListe=[]

yeniListe = liste1[:3]+liste1[4:]
print(yeniListe)


#Listeyi tersine cevirme 1 .yol
dizi=[1,2,3,4,5,6,7,8,9,10]
yeniListe=[]

yeniListe=dizi[-1::-1]
print(yeniListe)

#Listeyi tersine cevirme 2.yol

dizim=[1,2,3,4,5,6,7,8,9,10]
uzunluk=len(dizim)
yeniDizim =[]

for i in range(uzunluk-1,-1,-1):
    yeniDizim+=[dizim[i]]
    
print(yeniDizim)




    

    
