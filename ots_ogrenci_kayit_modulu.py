import mysql.connector

try:
  vtb_ogrenci = mysql.connector.connect( # vtb veri tabani baglantisi
    host="localhost", # Server/Veritabanı sistemi (instance) adı.
    user="root", # Veritabanı kullanıcı adı
    password="1234", # Veritabanı sistemi(instance) şifresi
    database="ots"
  )
  secilen_ogr = vtb_ogrenci.cursor()
  secilen_ogr.execute("create table if not exists ogrenciler(id int, ad varchar(22), sinif varchar(10))")
#   vtlistesi = secilen.fetchall()
  print("Bağlantı tamam.")
except:
  print("Veritabanına bağlanırken bir hata oluştu.")


from PyQt6.QtWidgets import *

class KayitPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Öğrenci Kayıt")

        icerik = QVBoxLayout()

        icerik.addWidget(QLabel("Adı: "))
        self.adkutusu = QLineEdit()
        icerik.addWidget(self.adkutusu)
        

        icerik.addWidget(QLabel("Sınıfı: "))
        self.sinifkutusu = QLineEdit()
        icerik.addWidget(self.sinifkutusu)
        

        buton1 = QPushButton("Kaydet")
        icerik.addWidget(buton1)
        buton1.clicked.connect(self.kaydetme)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def kaydetme(self):
        self.ad = self.adkutusu.text()
        self.sinif = self.sinifkutusu.text()
        print(f"Kaydedilecek bilgiler: {self.ad}, {self.sinif}")
        # self.label1.setText("yeni metin")
        # self.label1.setText(self.label1.text()+self.yazmakutusu.text()*2)
        secilen_ogr.execute(f"insert into ogrenciler(ad,sinif) values('{self.ad}','{self.sinif}')")
        vtb_ogrenci.commit()
        # self.label1.setText("Sonuç : "+str((int(self.yazmakutusu.text())*2)))
