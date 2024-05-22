#Dongu ile surekli 10 tane sayi aldiktan sonra bir listeye atan ardindan listedeki elemanlarin toplamini ekrana bastiran algoritma.
#1.Yol
sayilar =[]
for i in range(10):
    i=int(input("Sayi giriniz :"))
    sayilar.append(i)

print("Listedeki sayilarin toplami = %d" % (sum(sayilar)))


#2.Yol

sayilar =[]
for i in range(10):
    i=int(input("Bir sayi giriniz: "))
    sayilar.append(i)
    
toplam =0
for j in sayilar:
    toplam+=j
print(toplam)
