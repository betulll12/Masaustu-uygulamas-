from PyQt6.QtWidgets import (QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from moduller.word import WordWindow
from moduller.quiz import QuizWindow
from moduller.grammer_calismasi import GramerWindow
from moduller.ilerleme_raporu import IlerlemeWindow

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("English Learning Assistant - Ana Menü")
        self.setFixedSize(400, 350)

        # Ana layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Başlık
        baslik = QLabel("📘 Ana Menü")
        baslik.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        baslik.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(baslik)
        layout.addWidget(QLabel("Bir seçenek seçiniz:"))

        # Buton ayar fonksiyonu
        def ayarla_buton(buton, renk="#2196F3"):
            buton.setFixedWidth(200)
            buton.setStyleSheet(f"""
                QPushButton {{
                    background-color: {renk};
                    color: white;
                    border-radius: 10px;
                    font-size: 14px;
                    padding: 8px;
                }}
                QPushButton:hover {{
                    background-color: #1976D2;
                }}
            """)

        # Kelime Öğren
        buton_kelime = QPushButton("📚 Kelime Öğrenme")
        ayarla_buton(buton_kelime, "#4CAF50")
        buton_kelime.clicked.connect(self.kelime_ekrani)
        layout.addWidget(buton_kelime, alignment=Qt.AlignmentFlag.AlignCenter)

        # Quiz
        buton_quiz = QPushButton("📝 Quiz Yap")
        ayarla_buton(buton_quiz, "#FF9800")
        buton_quiz.clicked.connect(self.quiz_ekrani)
        layout.addWidget(buton_quiz, alignment=Qt.AlignmentFlag.AlignCenter)

        # Gramer
        buton_gramer = QPushButton("📖 Gramer Çalışması")
        ayarla_buton(buton_gramer, "#9C27B0")
        buton_gramer.clicked.connect(self.gramer_ekrani)
        layout.addWidget(buton_gramer, alignment=Qt.AlignmentFlag.AlignCenter)

        # İlerleme
        buton_ilerleme = QPushButton("📊 İlerleme Raporu")
        ayarla_buton(buton_ilerleme, "#F44336")
        buton_ilerleme.clicked.connect(self.ilerleme_ekrani)
        layout.addWidget(buton_ilerleme, alignment=Qt.AlignmentFlag.AlignCenter)

        # Çıkış
        buton_cikis = QPushButton("❌ Çıkış")
        ayarla_buton(buton_cikis, "#607D8B")
        buton_cikis.clicked.connect(self.close)
        layout.addWidget(buton_cikis, alignment=Qt.AlignmentFlag.AlignCenter)

        # Central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def kelime_ekrani(self):
        self.word_window = WordWindow()
        self.word_window.show()

    def quiz_ekrani(self):
        self.quiz_window = QuizWindow()
        self.quiz_window.show()

    def gramer_ekrani(self):
        self.gramer_window = GramerWindow()
        self.gramer_window.show()

    def ilerleme_ekrani(self):
        self.ilerleme_window = IlerlemeWindow()
        self.ilerleme_window.show()
