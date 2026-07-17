from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
class Magnet:

	def __init__(self):
		self.x = 0
		self.y = 0
		self.angle = 0
		self.speed = 20
		self.sprite = QPixmap("assets/images/split_rectangle.png").scaled(
			200,
			100,
			Qt.KeepAspectRatio,
			Qt.SmoothTransformation
		)
		self.width = self.sprite.width()
		self.height = self.sprite.height()

	def move_up(self):
		self.y -= self.speed

	def move_down(self):
		self.y += self.speed

	def move_left(self):
		self.x -= self.speed

	def move_right(self):
		self.x += self.speed

	def rotate_left(self):
		self.angle -= 15

	def rotate_right(self):
		self.angle += 15