import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("English Learning Asistant Uygulaması")
window.setFixedWidth(300)
window.setFixedHeight(200)

layout = QVBoxLayout() # layout = QHBoxLayout()
layout.addWidget(QLabel("Kullanıcı adı:"))
ka = QLineEdit()
layout.addWidget(ka)
layout.addWidget(QLabel("Şifre:"))
sf = QLineEdit()
sf.setEchoMode(QLineEdit.EchoMode.Password)  # şifre gizleme
layout.addWidget(sf)

layout.addWidget(QCheckBox("Beni hatırla"))

def kontrol():
    print(ka.text())
    print(sf.text())
    if ka.text() == "Betül" and sf.text() == "123": 
        print("giris yapabilir")
        QMessageBox.information(window, "Başarılı", "Giriş başarılı, hoş geldin!")
    else:
        print("izin yok")
        QMessageBox.warning(window, "Hata", "Kullanıcı adı veya şifre yanlış!")

buton = QPushButton("Giriş yap")
layout.addWidget(buton)
buton.clicked.connect(kontrol)
layout.addWidget(QLabel("..."))

widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)
window.show()
app.exec()
