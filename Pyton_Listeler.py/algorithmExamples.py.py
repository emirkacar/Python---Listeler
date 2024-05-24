sayilar=[10,12,13,14,15,16,17]
bilgiler = ["Emir","Kacar"]

birlestir=sayilar+bilgiler
print(birlestir)

print(4*sayilar)

print(sayilar)
sayilar[0:3]=[100,200,300,400,500]
print(sayilar)


listem=[10,20,30]

listem.clear()
print(listem)

listem=[10,20,30]
a=listem.pop(0)
print(listem)


sayilarim=[10,20,30,40,50,60,70,80,90,100]
print(sayilarim)

numbers=[1,2,3,100]
print(min(numbers))
print(max(numbers))
print(sum(numbers))





toplam=0
i=0
sayac=0
while(i<len(numbers)):
    toplam+=numbers[i]
    i+=1
    sayac+=1
print(toplam)
print("Ortalama = %.2f" % float(toplam/sayac))

numbers2= [1,2,3,4,100,16,15,17,20,13]
a=[]
a=numbers2.reverse()
print(a)






