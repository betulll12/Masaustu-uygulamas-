from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class IlerlemeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("İlerleme Raporu")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("İlerleme raporu ekranı buraya gelecek"))
        self.setLayout(layout)
