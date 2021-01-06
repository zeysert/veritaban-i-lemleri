import  sqlite3

baglanti = sqlite3.connect("Personel.db")
imlec = baglanti.cursor()
tablo= "CREATE TABLE IF NOT EXISTS kisiler(İsim TEXT,Soyisim TEXT,Bolum TEXT,Adres TEXT,No INT)"
imlec.execute(tablo)
baglanti.commit()
def baglanti_kes():
        baglanti.close()
def kisileri_goster():
        goster ="SELECT *FROM kisiler"
        imlec.execute(goster)
        kisiler =imlec.fetchall()
        if len(kisiler)==0:
            print("Sistemde kayıtlı kimse yok")
        else:
            for i in kisiler:
                print(i)

def kisi_bul(no):
        sorgu="SELECT * FROM kisiler WHERE no =?"
        imlec.execute(sorgu,(no,))
        kisiler =imlec.fetchall()
        if len(kisiler)==0:
            print("Aranılan Kişi Sistemde Bulunmamaktadır..")
        else:
            print(kisiler)

def kisi_ekle(isim, soyisim, bolum, adres, no):
        ekle ="INSERT INTO kisiler VALUES(?,?,?,?,?)"
        imlec.execute(ekle,(isim,soyisim,bolum,adres,no))
        baglanti.commit()
def kisi_sil(no):
        sorgu="DELETE FROM kisiler WHERE no = ?"
        imlec.execute(sorgu,(no,))
        baglanti.commit()

print("""
**************************************
1. Ekleme 
2. Arama
3. Listeleme
4. Silme
q. Çıkış
**************************************
""")

while True:
    islem= input("Bir işlem seçin :")
    if islem=="q":
          print("Çıkış Yapıldı")
          baglanti_kes()
          break
    elif islem=="1":
        isim = input("İsim :")
        soyisim = input("Soyisim :")
        bolum = input("Bölüm :")
        adres = input("Adres :")
        no = int(input("No :"))
        kisi_ekle(isim, soyisim, bolum, adres, no)
        print("Kişi Eklendi")
        
    elif islem=="2":
        no =input("Aranacak kişinin kayıt no: ")
        print("Kişi sorgulanıyor ...")
        kisi_bul(no)
        
    elif islem=="3":
        kisileri_goster()
        
    elif islem=="4":
        no =int(input("Silinecek kişinin kayıt no: "))
        tekrar =input("Kaydı silmek istediğinizden emin misiniz(E/H):")
        if tekrar=="E":
            print("Kayıt Silindi")
            kisi_sil(no)

    else:
        print("Geçersiz işlem")