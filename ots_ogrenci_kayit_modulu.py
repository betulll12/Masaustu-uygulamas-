import mysql.connector
from PyQt6.QtWidgets import *

# Veritabanı bağlantısı
try:
    vtb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="ots"
    )
    cursor = vtb.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            password VARCHAR(50)
        )
    """)
    print("Bağlantı tamam.")
except Exception as e:
    print("Veritabanına bağlanırken hata:", e)


class KayitPenceresi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kayıt Ol")

        icerik = QVBoxLayout()

        icerik.addWidget(QLabel("Kullanıcı Adı:"))
        self.username_input = QLineEdit()
        icerik.addWidget(self.username_input)

        icerik.addWidget(QLabel("Şifre:"))
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        icerik.addWidget(self.password_input)

        kaydet_btn = QPushButton("Kayıt Ol")
        kaydet_btn.clicked.connect(self.kaydet)
        icerik.addWidget(kaydet_btn)

        araclar = QWidget()
        araclar.setLayout(icerik)
        self.setCentralWidget(araclar)

    def kaydet(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı ve şifre boş olamaz!")
            return

        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            vtb.commit()
            QMessageBox.information(self, "Başarılı", "Kayıt tamamlandı!")
        except mysql.connector.Error as e:
            QMessageBox.warning(self, "Hata", f"Kayıt yapılamadı: {e}")
