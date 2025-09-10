from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class WordWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kelime Öğrenme")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Kelime öğrenme ekranı buraya gelecek"))
        self.setLayout(layout)
