import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QHBoxLayout
from PyQt5.QtGui import QPainter, QPen, QImage
from PyQt5.QtCore import Qt, QPoint
import numpy as np
from ml_model import predict_digit

class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(280, 280)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.last_point = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.drawing:
            painter = QPainter(self.image)
            pen = QPen(Qt.black, 15, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
            painter.setPen(pen)
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.image, self.image.rect())

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def get_image(self):
        ptr = self.image.bits()
        ptr.setsize(self.image.byteCount())
        arr = np.array(ptr).reshape(self.image.height(), self.image.width(), 4)
        gray = 255 - arr[:, :, 0]
        gray = gray / 255.0
        gray = gray.reshape(1, 280, 280, 1)
        return gray

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("El Yazısı Rakam Tanıma")
        self.canvas = Canvas()
        self.result_label = QLabel("Tahmin: ")
        self.result_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.clear_button = QPushButton("Temizle")
        self.clear_button.clicked.connect(self.canvas.clear)

        self.predict_button = QPushButton("Tahmin Et")
        self.predict_button.clicked.connect(self.predict)

        vbox = QVBoxLayout()
        vbox.addWidget(self.canvas)
        vbox.addWidget(self.clear_button)
        vbox.addWidget(self.predict_button)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox)
        hbox.addWidget(self.result_label)

        self.setLayout(hbox)

    def predict(self):
        img = self.canvas.get_image()
        digit = predict_digit(img)
        self.result_label.setText(f"Tahmin: {digit}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
