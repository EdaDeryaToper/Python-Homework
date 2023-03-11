#Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.
#Sayılar:
sayi1=10 #integer
sayi2=100.10 #float
sayi3=3.14j #complex

#Yazı-Karakter:
yazi1="Merhaba"
yazi2='Merhaba'
yazi3='M'

#Liste, tuple, dictionary
liste1=[sayi1,sayi2,sayi3,yazi1,yazi2,yazi3]
tuple1=(sayi1,sayi2,sayi3,yazi1,yazi2,yazi3)
dictionary1={'integer': sayi1, 'float': sayi2, 'complex': sayi3, 'string': yazi1, 'liste': liste1}
for i in dictionary1:
    print(i, " : ", dictionary1[i])

#Kodlama.io sitesinde değişken olarak kullanıldığını düşündüğünüz verileri, veri tipleriyle birlikte örneklendiriniz.
kategori = "Kategori" #string
egitmen= ["Engin Demiroğ", "Halit Enes Kalaycı"] #list
egitimTamamlanmaYuzdesi = 0 #int
clickButton= True #bool


#Kodlama.io sitesinde şart blokları kullanıldığını düşündüğünüz kısımları örneklendiriniz ve Python dilinde bu örnekleri koda dökünüz.
#"Bitir ve devam et" buton tıklanmasına göre Eğitim tamamlanma yüzdesi:
egitimDersSayisi=20
for i in range(egitimDersSayisi):
    if(clickButton):
      egitimTamamlanmaYuzdesi = i*5
      print(i, egitimTamamlanmaYuzdesi)
print(egitimTamamlanmaYuzdesi + 5)