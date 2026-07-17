#game.py
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtWidgets import QWidget, QMainWindow
from PySide6.QtCore import Qt
import os
from src.level import Level
from src.game_objects import Magnet, Ball, Hole
from src.physics import boundary_collision

class GameWindow(QMainWindow):
	def __init__(self):
		super().__init__()

		self.setWindowTitle("Magneto Ball")
		self.resize(1200,720)

		self.game_widget = GameWidget()
		self.setCentralWidget(self.game_widget)
		self.adjustSize()

class GameWidget(QWidget):
	def __init__(self):
		super().__init__()

		self.setFixedSize(1200, 720)
		self.setFocusPolicy(Qt.StrongFocus)
		self.setFocus()

		#assets
		self.background = QPixmap("assets/images/background_brown.png")
		self.ball = Ball()
		self.hole = Hole()
		self.magnet = Magnet()

		self.level = Level(self)
		self.level.new_level()
		#print(self.ball.isNull())
		#print(self.hole.isNull())

	def paintEvent(self, event):
		painter = QPainter(self)

		scaled_background = self.background.scaled(
			self.size(), Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
		painter.drawPixmap(0, 0, scaled_background)

		painter.drawPixmap(self.hole.x, self.hole.y, self.hole.sprite)
		painter.drawPixmap(self.ball.x, self.ball.y, self.ball.sprite)
		painter.drawPixmap(self.magnet.x, self.magnet.y, self.magnet.get_rotated_sprite())

		painter.end()

	# game.py
	def keyPressEvent(self, event):

		if event.key() == Qt.Key_W:
			self.magnet.move_up()

		elif event.key() == Qt.Key_S:
			self.magnet.move_down()

		elif event.key() == Qt.Key_A:
			self.magnet.move_left()

		elif event.key() == Qt.Key_D:
			self.magnet.move_right()

		elif event.key() == Qt.Key_Right:
			self.magnet.rotate_right()

		elif event.key() == Qt.Key_Left:
			self.magnet.rotate_left()

		self.update_game()

	def update_game(self):
	    boundary_collision(self.magnet, self)
	    boundary_collision(self.ball, self)
	    self.update()