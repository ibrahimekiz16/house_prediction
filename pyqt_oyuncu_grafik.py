import sys
import json
import matplotlib
matplotlib.use("Qt5Agg")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit
)
from PyQt5.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import mplcursors

class PlayerStats(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Oyuncu İstatistik Görüntüleyici")
        self.setGeometry(100, 100, 400, 500)

        self.layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Oyuncu adı girin...")
        self.layout.addWidget(self.name_input)

        self.button = QPushButton("Verileri Göster")
        self.button.clicked.connect(self.show_data)
        self.layout.addWidget(self.button)

        self.info_label = QLabel()
        self.layout.addWidget(self.info_label)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

        with open("C:/Users/ibrah/Projelerim/playerdata.json", "r", encoding="utf-8") as f:

            self.players = json.load(f)

    def show_data(self):
        player_name = self.name_input.text().strip().lower()
        if not player_name:
            self.info_label.setText("Lütfen bir oyuncu adı girin.")
            self.ax.clear()
            self.canvas.draw()
            return

        player = self.players.get(player_name)
        if not player:
            self.info_label.setText("Oyuncu bulunamadı.")
            self.ax.clear()
            self.canvas.draw()
            return

        goals = player["goals"]
        shots = player["shots"]
        height = player["height"]
        weight = player["weight"]

        self.info_label.setText(f"Boy: {height} | Kilo: {weight}")

        self.ax.clear()
        bars = self.ax.bar(['Şut', 'Gol'], [shots, goals], color=['blue', 'green'])
        self.ax.set_title(f"{player_name.capitalize()} İstatistikleri")
        self.ax.set_ylim(0, max(shots, goals) + 10)
        self.canvas.draw()

        cursor = mplcursors.cursor(bars, hover=True)

        @cursor.connect("add")
        def on_add(sel):
            sel.annotation.set_text(f"{int(sel.target[1])}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PlayerStats()
    window.show()
    sys.exit(app.exec_())
