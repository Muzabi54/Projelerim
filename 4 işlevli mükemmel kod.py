a=20
b=80

toplam=a+b
fark  =a-b
carp  =a*b
bol   =a/b

print("Toplam",toplam)
print("Toplam",fark)
print("Toplam",carp)
print("Toplam",bol)
    
ad="Melih"
soyad="Ozan"
yas="15"
okul_adi="Adapazari Anadolu İmamhatip Lisesi Fen ve Sosyal Bilimler Proje Okulu"
okul_no="461"
fav_ders="İngilizce"

print("Ad=",ad)
print("Soy Adı=",soyad)
print("Yaşı=",yas)
print("Okul=",okul_adi)
print("Okul numara=",okul_no)
print("Favori Ders=",fav_ders)

ad=input("İsmin ne?")
soyad=input("Soyadın ne?")
yas=int(input("Yaş kaç birader?"))
ıq=(input("Yaserin IQ kaç?"))
yetenek=input("Yeteneğin var mı?")
beyin_yas=int(input("Beyin yaşı kaç?"))


print("İsim :",ad)
print("Soyisim :",soyad)
print("Yaş :",yas)
print("Yaser IQ :",ıq)
print("Yaserin yetenekleri :",yetenek)
print("Yaserin Beyin Yaşı :",beyin_yas)

yaz_1=int(input("İlk yazılı kaç geldi?"))
yaz_2=int(input("Peki ikinci yazılı kaç geldi?"))
per_1=int(input("Hoca ilk sözlüye kaç verdi?"))
per_2=int(input("İkinci sözlü kaç geldi?"))
proje=int(input("Proje notu kaç?"))

toplam=yaz_1+yaz_2+per_1+per_2+proje

ort= toplam/5
print("Karne Ortalaması",ort)

metin="Mortingen Şitraze"
print (metin [0])
print (metin [4:7])
print (metin [8::])
print (metin [-2])
print (metin [:7])
print (metin [8:])
print (metin [0:8:2])
print (metin)


yaz_1=int(input("İlk yazılı kaç geldi?"))
yaz_2=int(input("Peki ikinci yazılı kaç geldi?"))
per_1=int(input("Hoca ilk sözlüye kaç verdi?"))
per_2=int(input("İkinci sözlü kaç geldi?"))
proje=int(input("Proje notu kaç?"))

toplam=(yaz_1+yaz_2+per_1+per_2+proje)
ort= toplam/5
if(ort<50):
    print("Notun:",ort)
    print("Zorrrt kaldın")
else:
    print("Notun:",ort)
    print("Afferin geçtin")

yas= int(input("Yaşını söyle"))
yas31= int(input("Arkdaşnın yaşını söyle"))
if(yas31>63):
    print("Arkadaşın haddi aşmış")
if(yas>63):
          print("Haddi aşmışsın")
if(yas>yas31):
    print("Afferim arkadaşından büyüksün iyi halt yedin")

elif(yas==yas31):

    print("Yaşıtsınız")

else:
    print("Arkadaşından küçüksün artık bu bilgiyi nabarsan yap")


sayi= int(input("Tek ya da Çift olup olmadığını merak ettiğin sayıyı yaz:"))
modu= sayi%2
if(modu==0):
    print("Sayı çifttir hadi iyi günler")
else:
    print("Sayı tektir hadi iyi günler")


sayi3169= int(input("Sayının yedi ile bölünmediğini bulmak için sayı yaz:"))
mod= sayi3169%7

if(mod==0):
    print("7ye tam bölünüyor")

else:
    print("7ye bölünmüyor")

sayi3169= int(input("Sayı gir 7 ve 12 ye bölünüp bölünmediğini bulayım"))
mod31= sayi3169%7
mod3169= sayi3169%12

if(mod31==0and(mod3169==0)):
   print("Hem 7 hem de 12 ye bölünüyor")

elif((mod31!=0)and(mod3169==0)):
    print("7ye bölünmüyor ama üzülme 12ye bölünüyor")

   
















    
