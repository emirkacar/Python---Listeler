##En buyuk sayiyi bulan algoritma 1.Yol

sayilar = [10, 25, 12, 78, 3]
max=sayilar[0]

for i in sayilar:
    if(max<i):
        max=i
print(max)


#En buyuk sayiyi bulan algoritma 2.Yol
sayilar = [10, 25, 12, 78, 3]
max=sayilar[0]

for i in range(len(sayilar)):
    if(max<sayilar[i]):
        max=sayilar[i]
print(max)