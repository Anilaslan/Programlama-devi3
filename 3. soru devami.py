from etkilesimHesabi import etkilesimOraniHesapla

ybs1=etkilesimOraniHesapla(365000,65000,870,500,1125000)
ybs2=etkilesimOraniHesapla(450000,25000,380,100,1450000)
ybs3=etkilesimOraniHesapla(582000,52000,1200,650,2000000)

def hesap(a):
    if a>0.2:
        print(round((a),2),"Etkileşim oranı yüksek")
    else:
        print(round((a),2),"Etkileşim oranı düşük")

print("YBS-1")
hesap(ybs1)
print("YBS-2")
hesap(ybs2)
print("YBS-3")
hesap(ybs3)
