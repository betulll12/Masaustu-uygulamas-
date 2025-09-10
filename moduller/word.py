from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QListWidget
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class WordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kelime Öğrenme")
        self.setFixedSize(350, 300)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        baslik = QLabel("📚 Kelime Öğrenme")
        baslik.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(baslik)

        # Örnek kelimeler listesi
        kelime_listesi = QListWidget()
        kelime_listesi.addItems([
            "Apple - Elma",
            "Book - Kitap",
            "House - Ev",
            "Car - Araba",
            "Computer - Bilgisayar"
        ])
        kelime_listesi.setFixedHeight(150)
        layout.addWidget(kelime_listesi)

        self.setLayout(layout)
