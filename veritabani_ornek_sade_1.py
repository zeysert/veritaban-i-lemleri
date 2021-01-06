import sqlite3
okul = sqlite3.connect('deneme.db')
imlec = okul.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS ogrenci(Ogr_adi TEXT,Ogr_soyadi TEXT,Ogr_no INT,Ogr_yas INT)")

print(""" 
1.) Yeni Kayit 
2.) Kayit Guncelle 
3.) Tum Kayitlari Goster 
4.) Kayit Ara 
5.) Kayit Sil 
0.) Cikis """)

while True: 
    select = int(input('İşlem seçiniz :')) 
    if select==1: 
        Ogr_adi = input('Ogrenci ismi girin :') 
        Ogr_soyadi = input('Ogrenci soyadi girin :') 
        Ogr_no = int(input('Ogrenci no girin :')) 
        Ogr_yas = int(input('Ogrenci yas girin :')) 
        imlec.execute('INSERT INTO ogrenci(Ogr_adi,Ogr_soyadi,Ogr_no,Ogr_yas) VALUES(?,?,?,?)',(Ogr_adi,Ogr_soyadi,Ogr_no,Ogr_yas))
        okul.commit()
    elif select==2: 
        imlec.execute('UPDATE ogrenci SET Ogr_adi = "Mert" WHERE Ogr_yas = 20')
        okul.commit()
    elif select==3: 
       imlec.execute('SELECT * FROM ogrenci') 
       ogrenciler = imlec.fetchall() 
       for i in ogrenciler: 
          print(i) 
    
    elif select==4: 
        Ogr_no = int(input('Aranacak öğrenci numarasini girin :')) 
        imlec.execute('SELECT * FROM ogrenci WHERE Ogr_no ={}'.format(Ogr_no)) 
        kisi = imlec.fetchall() 
        print(kisi) 
    elif select==5: 
        Ogr_no = int(input('Silinecek öğrenci numarasini girin :')) 
        imlec.execute('DELETE FROM ogrenci WHERE Ogr_no={}'.format(Ogr_no)) 
        okul.commit()
        print("Kayıt Silindi")
    elif select==0: 
        exit()