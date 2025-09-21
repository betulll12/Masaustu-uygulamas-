# -------------------------------------
# Veri tabanı bağlantısı
import mysql.connector

try:
    vtb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234"
    )
    secilen = vtb.cursor()
    secilen.execute("CREATE DATABASE IF NOT EXISTS ots")
    secilen.execute("USE ots")
    print("Bağlantı tamam ✅")
except:
    print("Veritabanına bağlanırken bir hata oluştu.")

# -------------------------------------
from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İngilizce Kelime Öğrenme")

        def kelimeEkle():
            kelime_eng, ok1 = QInputDialog.getText(self, "Kelime Ekle", "İngilizce:")
            kelime_tr, ok2 = QInputDialog.getText(self, "Kelime Ekle", "Türkçe:")
            if ok1 and ok2 and kelime_eng and kelime_tr:
                secilen.execute("INSERT INTO kelimeler (ingilizce, turkce) VALUES (%s, %s)", 
                                (kelime_eng, kelime_tr))
                vtb.commit()
                QMessageBox.information(self, "Bilgi", "Kelime başarıyla eklendi ✅")

        def kelimeListele():
            secilen.execute("SELECT * FROM kelimeler")
            veriler = secilen.fetchall()
            text = ""
            for row in veriler:
                text += f"{row[1]} - {row[2]}\n"
            QMessageBox.information(self, "Kelimeler", text if text else "Henüz kelime yok!")

        def quizYap():
            secilen.execute("SELECT ingilizce, turkce FROM kelimeler ORDER BY RAND() LIMIT 1")
            soru = secilen.fetchone()
            if not soru:
                QMessageBox.warning(self, "Uyarı", "Önce kelime eklemelisin!")
                return
            cevap, ok = QInputDialog.getText(self, "Quiz", f"{soru[0]} kelimesinin Türkçesi nedir?")
            if ok:
                if cevap.lower() == soru[1].lower():
                    QMessageBox.information(self, "Sonuç", "Doğru ✅")
                else:
                    QMessageBox.information(self, "Sonuç", f"Yanlış ❌ Doğru cevap: {soru[1]}")

        icerik = QVBoxLayout()

        buton1 = QPushButton('Kelime Ekle')
        buton1.clicked.connect(kelimeEkle)
        icerik.addWidget(buton1)

        buton2 = QPushButton('Kelimeleri Listele')
        buton2.clicked.connect(kelimeListele)
        icerik.addWidget(buton2)

        buton3 = QPushButton('Quiz Yap')
        buton3.clicked.connect(quizYap)
        icerik.addWidget(buton3)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

# -------------------------------------
class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kelime Uygulaması - Giriş")
        self.setFixedWidth(300)
        self.setFixedHeight(200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Kullanıcı adı:"))
        self.ka = QLineEdit()
        layout.addWidget(self.ka)

        layout.addWidget(QLabel("Şifre:"))
        self.sf = QLineEdit()
        self.sf.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.sf)

        btn_giris = QPushButton("Giriş yap")
        btn_giris.clicked.connect(self.kontrol)
        layout.addWidget(btn_giris)

        btn_kayit = QPushButton("Kayıt ol")
        btn_kayit.clicked.connect(self.kayitOl)
        layout.addWidget(btn_kayit)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()

    def kontrol(self):
        secilen.execute("SELECT * FROM kullanicilar WHERE username=%s AND password=%s", 
                        (self.ka.text(), self.sf.text()))
        kullanici = secilen.fetchone()
        if kullanici:
            self.anaekran = AnaPencere()
            self.anaekran.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")

    def kayitOl(self):
        secilen.execute("INSERT INTO kullanicilar (username, password) VALUES (%s, %s)", 
                        (self.ka.text(), self.sf.text()))
        vtb.commit()
        QMessageBox.information(self, "Bilgi", "Kayıt başarılı ✅ Artık giriş yapabilirsiniz.")

# -------------------------------------
app = QApplication([])
pencere = GirisEkrani()
pencere.show()
app.exec()
