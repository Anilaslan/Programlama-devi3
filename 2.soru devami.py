from bilancoHesabi import aktif,pasif

doVarlik=int(input("Toplam dönen varlık: "))
duVarlik=int(input("Toplam duran varlık: "))

aktifToplami=aktif(doVarlik,duVarlik)

kSureliBorc=int(input("Kısa vadeli borç toplamı: "))
uSureliBorc=int(input("Uzun vadeli borç toplamı: "))
ozkaynak=int(input("Özkaynaklar toplamı: "))

pasifToplami=pasif(kSureliBorc,uSureliBorc,ozkaynak)

bilancoKontrol=aktifToplami-pasifToplami

if bilancoKontrol==0:
    print("Bilanço hesabı doğru",pasifToplami,"lira")
else:
    print("Bilanço hesabı yanlış!Değerler arasında",abs(bilancoKontrol),"lira fark var.")
