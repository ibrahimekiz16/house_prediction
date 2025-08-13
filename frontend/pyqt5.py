import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton,
    QVBoxLayout, QStackedWidget, QLabel
)
from PyQt5.QtCore import QPropertyAnimation, QRect, QEasingCurve


class Sayfa1(QWidget):
    def __init__(self, parent):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("Hoşgeldin! Bu Giriş Sayfası", self)
        self.buton = QPushButton("Devam Et", self)
        self.buton.clicked.connect(parent.sayfa_degistir)

        layout.addWidget(self.label)
        layout.addWidget(self.buton)
        self.setLayout(layout)


class Sayfa2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        self.label = QLabel("Burası Ana Sayfa", self)
        layout.addWidget(self.label)
        self.setLayout(layout)


class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Animasyonlu Sayfa Geçişi")
        self.setGeometry(200, 200, 400, 300)

        self.stack = QStackedWidget()
        self.sayfa1 = Sayfa1(self)
        self.sayfa2 = Sayfa2()

        self.stack.addWidget(self.sayfa1)
        self.stack.addWidget(self.sayfa2)

        self.setCentralWidget(self.stack)

    def sayfa_degistir(self):
        # Sayfa2 animasyonla gelsin
        self.stack.setCurrentWidget(self.sayfa2)

        # Geçiş animasyonu
        self.sayfa2.setGeometry(QRect(400, 0, 400, 300))  # Başlangıç konumu (sağdan)
        self.anim = QPropertyAnimation(self.sayfa2, b"geometry")
        self.anim.setDuration(500)
        self.anim.setStartValue(QRect(400, 0, 400, 300))
        self.anim.setEndValue(QRect(0, 0, 400, 300))
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())
