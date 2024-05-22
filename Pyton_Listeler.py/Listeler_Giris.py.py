mixed = ["Bursa","Ankara","Edirne",[15,16,17,18]]
print(mixed)



a=[10,20,30,40,50,60]
a[0]=16
print(a) 




a = [1, 2, 3]
b = a

print("a:", a)  # a: [1, 2, 3]
print("b:", b)  # b: [1, 2, 3]

# b'yi değiştirirsek a da etkilenir
b.append(4)

print("a:", a)  # a: [1, 2, 3, 4]
print("b:", b)  # b: [1, 2, 3, 4]



liste=[1,2,3,4,5,6]
liste1=[100,200,300,400]

print(liste * 3)





liste=[1,2,3,4,5,6]
liste1=[100,200,300,400]

c=(liste+liste1)
print(c)


a=[10,20,30,40,50]
print(len(a))
print(min(a))
print(max(a))




#SUM FONKSİYONUNUN KULLANIMI
a=[10,20,30,40,50]
toplam=sum(a,100)
print(toplam)


#DEL FONKSİYONUNUN KULLLANIMI
sayilar=[1,2,3,4,5]
print(sayilar)
c=sayilar.pop(0)
print(sayilar)

#Sorted fonksiyonunun kullanimi
sayilar=[2,5,15,14,19,26,32,0]
print(sorted(sayilar))


isimler=["Emir","Ahmet","Tuncay"]
print(sorted(isimler))


sayilar = [10,20,30,15,50,40,75,60,25,35]

adet = 0
for i in sayilar:
    adet+=1
print("Sayilar listesinde %d tane sayi vardir." % (adet))  # % ile ekrana bastirma.
print(f"Sayilar listesinde {adet} tane sayi vardir.") # f string ile ekrana bastirma.
print("Sayilar listesinde {} tane sayi vardir." .format(adet)) # .format ile ekrana bastirma.














