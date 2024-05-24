#Palindrom kelimeyi bulma algoritmasi 1.yol
"""kelime = input("Bir kelime giriniz : ")
palindrome=False
for i in range(len(kelime)//2):
    if(kelime[i]==kelime[-1]):
        palindrome=True

if(palindrome):
    print("Kelime palindromedur.")
else:
    print("Kelime palindrom degildir.")"""



#Palindrom kelimeyi bulma algoritmasi (2.yol)

kelime = input("Bir kelime giriniz : ")
tersKelime=""
for i in kelime[::-1]:
    tersKelime+=i

if(kelime==tersKelime):
    print("Kelime palindromedur.")
else :
    print("Kelime palindrome degildir.")