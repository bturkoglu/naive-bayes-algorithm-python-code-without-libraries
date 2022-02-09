# Navie
#dizin = "C:/Users/ali ihsan/Desktop/Çocuklar/Bahaeddin/Navie/"

#kosullar tablosunu okuyalım.


kosul = []
with open('kosullar.txt') as f:
    for line in f:
        satir = line.strip().split(sep='\t')[1:]
        kosul.append(satir)

#Parametreleri (hava, sıcaklık, nem vs.) ve değerlerini ayıralım.
parametreler = kosul[0]
ParametreDegerleri = {}

for i in range(len(parametreler)):
    degerler = []
    for deger in kosul[1:]:
        if deger[i] not in degerler:
            degerler.append(deger[i])
    ParametreDegerleri[parametreler[i]] = degerler

#print(ParametreDegerleri)    

#istenen okutulması
def isteneniOku():
    soru = []
    SorulanParametre = ''
    for parametre in parametreler:
        degerler = ParametreDegerleri[parametre]
        mesaj = parametre + ' değerini giriniz:'
        if SorulanParametre == '': mesaj += '(sonuç için ? seçiniz)'
        print()
        print(mesaj)
        print('='*len(mesaj))
        for i,d in enumerate(degerler,1):
            print(i,'.',d)

        while True:
            a = input('\t \t Seçiniz:')
            if a == '?':
                if SorulanParametre == '':
                    SorulanParametre = parametre
                    soru.append('?')
                    break
                else:
                    print('Daha önce ? girildi. Lütfen doğru değer giriniz')
                    continue
            else:
                
                if a.isdigit() and int(a) in range(1, len(degerler)+1):
                    soru.append(degerler[int(a)-1])
                    break
                else:
                    print('Lütfen geçerli bir değer giriniz!')

    return (soru, SorulanParametre)

def bilinenleriBas():
    print('Koşul Tablosu:')
    for line in kosul:
        print(line)
    print()
    print('Parametreler:', parametreler)
    print()
##    print('Parametre Degerleri:')
##    for line in ParametreDegerleri:
##        print(line)
##    print()
    print('Soru:',soru)
    print('SorulanParametre:',SorulanParametre)                     


#soru, SorulanParametre = isteneniOku()
soru = ['gunesli','serin','yuksek','guclu','?'];SorulanParametre = 'Karar'

bilinenleriBas()    

#SorulanParametrenin ihtimal hesaplarını bulalım.
sorulaninIndexi = parametreler.index(SorulanParametre)

#Sorulanın degerlerinin adetleri
adetler = {}
degerler = ParametreDegerleri[SorulanParametre]
for deger in degerler:
    adet = 0
    for line in kosul[1:]:
        if line[sorulaninIndexi] == deger: adet += 1
    adetler[deger] = adet

print('Adetler:', adetler)

toplam = len(kosul)-1

sonuc = {}
MaxValue = -1
MaxDeger = degerler[0]

for deger in degerler:
    sonucadetler = []
    hesap = adetler[deger]/toplam
    print()
    for i in range(len(soru)):
        param = soru[i]
        if param == '?':continue
        altkume = [line for line in kosul[1:] if line[sorulaninIndexi]==deger and line[i] == param]
        
        sonucadetler.append(len(altkume))
        
        print(SorulanParametre,':', deger, 've', parametreler[i],':',param, ' Adet:',len(altkume), '/',adetler[deger])
        #print(altkume)
        hesap = hesap * len(altkume)/adetler[deger]

    sonuc[deger]=(hesap, sonucadetler,adetler[deger],toplam)
    if MaxValue < hesap:
        MaxValue = hesap
        MaxDeger = deger

print()    
print('Sonuc Detay:')
for k,v in sonuc.items():
    print(k,"\t==>",v)

satirboyu = len(str(soru)) + 6    
print('='*satirboyu)
print('Soru:',soru)
print('Netice:', SorulanParametre,':', MaxDeger)
print('='*satirboyu)    
        

