from karveciro import isletmeKar
from karveciro import adam_basi_ciro

gelir=int(input("Toplam gelir:"))
gider=int(input("Toplan gider:"))

print("İşletmenizin kârı",isletmeKar(gelir,gider),"lira")

tCiro=int(input("Toplam ciro:"))
tCalisan=int(input("Toplam çalışan sayısı:"))

print("Adambaşı cironuz",adam_basi_ciro(tCiro,tCalisan),"lira")
