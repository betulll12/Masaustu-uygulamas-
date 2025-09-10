from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget
from moduller.word import WordWindow
from moduller.quiz import QuizWindow
from moduller.grammer_calismasi import GramerWindow
from moduller.ilerleme_raporu import IlerlemeWindow
import sys

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("English Learning Assistant - Ana Menü")
        self.setFixedSize(400, 300)  # Pencere boyutu

        layout = QVBoxLayout()
        layout.addWidget(QLabel("📘 Ana Menü"))
        layout.addWidget(QLabel("Bir seçenek seçiniz:"))

        # Kelime Öğren
        buton_kelime = QPushButton("📚 Kelime Öğrenme")
        buton_kelime.clicked.connect(self.kelime_ekrani)
        layout.addWidget(buton_kelime)

        # Quiz
        buton_quiz = QPushButton("📝 Quiz Yap")
        buton_quiz.clicked.connect(self.quiz_ekrani)
        layout.addWidget(buton_quiz)

        # Gramer
        buton_gramer = QPushButton("📖 Gramer Çalışması")
        buton_gramer.clicked.connect(self.gramer_ekrani)
        layout.addWidget(buton_gramer)

        # İlerleme
        buton_ilerleme = QPushButton("📊 İlerleme Raporu")
        buton_ilerleme.clicked.connect(self.ilerleme_ekrani)
        layout.addWidget(buton_ilerleme)

        # Çıkış
        buton_cikis = QPushButton("❌ Çıkış")
        buton_cikis.clicked.connect(self.close)
        layout.addWidget(buton_cikis)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec())
