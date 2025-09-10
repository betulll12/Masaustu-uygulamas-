import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QLabel, 
                             QLineEdit, QCheckBox, QPushButton, QWidget, QMessageBox)
from PyQt6.QtGui import QFont, QIcon
from PyQt6.QtCore import Qt
from anamenu import AnaPencere  # Ana Menü penceresi

class GirisEkrani(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("English Learning Assistant")
        self.setFixedSize(350, 250)

        # Ana layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Başlık
        baslik = QLabel("📚 Giriş Ekranı")
        baslik.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(baslik)

        # Kullanıcı adı
        layout.addWidget(QLabel("Kullanıcı adı:"))
        self.ka = QLineEdit()
        self.ka.setFixedWidth(200)
        self.ka.setStyleSheet("padding: 5px; font-size: 13px;")
        layout.addWidget(self.ka, alignment=Qt.AlignmentFlag.AlignCenter)

        # Şifre
        layout.addWidget(QLabel("Şifre:"))
        self.sf = QLineEdit()
        self.sf.setEchoMode(QLineEdit.EchoMode.Password)
        self.sf.setFixedWidth(200)
        self.sf.setStyleSheet("padding: 5px; font-size: 13px;")
        layout.addWidget(self.sf, alignment=Qt.AlignmentFlag.AlignCenter)

        # Beni hatırla
        self.beni_hatirla = QCheckBox("Beni hatırla")
        layout.addWidget(self.beni_hatirla, alignment=Qt.AlignmentFlag.AlignCenter)

        # Giriş butonu
        self.buton = QPushButton("Giriş yap")
        self.buton.setFixedWidth(150)
        self.buton.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border-radius: 10px;
                font-size: 14px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.buton.clicked.connect(self.kontrol)
        layout.addWidget(self.buton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Boşluk
        layout.addWidget(QLabel(""))

        # Central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def kontrol(self):
        if self.ka.text() == "Betül" and self.sf.text() == "123":
            QMessageBox.information(self, "Başarılı", "Giriş başarılı, hoş geldin!")
            self.ana_pencere = AnaPencere()
            self.ana_pencere.show()
            self.close()
        else:
            QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    giris = GirisEkrani()
    giris.show()
    sys.exit(app.exec())
