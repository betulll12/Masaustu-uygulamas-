from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class IlerlemeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İlerleme Raporu")
        self.setFixedSize(350, 300)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        baslik = QLabel("📊 İlerleme Raporu")
        baslik.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(baslik)

        # Örnek ilerleme verisi
        layout.addWidget(QLabel("Kelime Öğrenme: 10/20 kelime"))
        layout.addWidget(QLabel("Quiz Başarı Oranı: %75"))
        layout.addWidget(QLabel("Gramer Çalışması: 3/5 konu tamamlandı"))

        self.setLayout(layout)
