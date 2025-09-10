from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class GramerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gramer Çalışması")
        self.setFixedSize(350, 300)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        baslik = QLabel("📖 Gramer Çalışması")
        baslik.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(baslik)

        # Örnek gramer içeriği
        layout.addWidget(QLabel("Simple Present Tense:\nÖrnek: I eat an apple every day."))
        layout.addWidget(QLabel("Present Continuous:\nÖrnek: She is reading a book now."))

        self.setLayout(layout)
