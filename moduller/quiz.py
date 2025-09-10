from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class QuizWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Quiz Yap")
        self.setFixedSize(350, 300)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        baslik = QLabel("📝 Quiz")
        baslik.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(baslik)

        # Örnek soru
        soru = QLabel("Apple kelimesinin Türkçe karşılığı nedir?")
        soru.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(soru)

        # Cevap butonları
        def cevap(dogru):
            if dogru:
                QMessageBox.information(self, "Doğru!", "Tebrikler, doğru cevap!")
            else:
                QMessageBox.warning(self, "Yanlış", "Maalesef yanlış cevap!")

        btn1 = QPushButton("Elma")
        btn1.clicked.connect(lambda: cevap(True))
        btn2 = QPushButton("Araba")
        btn2.clicked.connect(lambda: cevap(False))
        layout.addWidget(btn1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(btn2, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

