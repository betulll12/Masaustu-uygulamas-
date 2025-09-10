from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class GramerWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gramer Çalışması")
        self.setFixedSize(300, 200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Gramer çalışması ekranı buraya gelecek"))
        self.setLayout(layout)
