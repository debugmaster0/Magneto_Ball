#game.py
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtCore import Qt
import os
from src.level import Level

class GameWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Magneto Ball")
		self.resize(1200,720)

		self.game_widget = GameWidget()
		self.setCentralWidget(self.game_widget)

class GameWidget(QWidget):
	def __init__(self):
		super().__init__()

		#assets
		self.background = QPixmap("assets/images/background_brown.png")
		self.ball = QPixmap("assets/images/ball_blue_small.png")
		self.hole = QPixmap("assets/images/hole.png")

		self.level = Level(self)
		self.level.new_level()
		#print(self.ball.isNull())
		#print(self.hole.isNull())

	def paintEvent(self, event):
		painter = QPainter(self)

		scaled_background = self.background.scaled(
			self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)

		painter.drawPixmap(0, 0, scaled_background)
		painter.drawPixmap(self.hole_x, self.hole_y, self.hole)
		painter.drawPixmap(self.ball_x, self.ball_y, self.ball)