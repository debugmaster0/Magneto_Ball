# level.py
import random
import math
from PySide6.QtCore import QRect

class Level:

	def __init__(self, game):
		self.game = game

	def new_level(self):
		self.place_hole()
		self.place_ball()
		self.place_magnet()

	def place_hole(self):
		#placement limits
		max_x = 1200 - self.game.hole.width()
		max_y = 720 - self.game.hole.height()
		mid_x = max_x // 2

		#random placement
		self.game.hole_x = random.randint(mid_x + self.game.hole.width()
			, max_x)
		self.game.hole_y = random.randint(0, max_y)

	def place_ball(self):
		max_x = self.game.width() - self.game.ball.width()
		max_y = self.game.height() - self.game.ball.height()
		mid_x = max_x // 2

		#random placement
		for _ in range(100):
			self.game.ball_x = random.randint(0, mid_x)
			self.game.ball_y = random.randint(0, max_y)

			distance = self.game.hole_x - self.game.ball_x

			if distance >= 450:
				break

	def place_magnet(self):
		max_x = self.game.width() - self.game.magnet.width
		max_y = self.game.height() - self.game.magnet.height

		ball_rect = QRect(
			self.game.ball_x,
			self.game.ball_y,
			self.game.ball.width(),
			self.game.ball.height()
		)

		hole_rect = QRect(
			self.game.hole_x,
			self.game.hole_y,
			self.game.hole.width(),
			self.game.hole.height()
		)

		for _ in range(100):
			magnet_x = random.randint(0, max_x)
			magnet_y = random.randint(0, max_y)

			magnet_rect = QRect(
				magnet_x,
				magnet_y,
				self.game.magnet.width,
				self.game.magnet.height
			)

			if not magnet_rect.intersects(ball_rect) and \
			   not magnet_rect.intersects(hole_rect):

				self.game.magnet.x = magnet_x
				self.game.magnet.y = magnet_y
				return