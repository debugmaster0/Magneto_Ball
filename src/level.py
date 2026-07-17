# level.py
import random
import math
from PySide6.QtCore import QRect

class Level:

	def __init__(self, game):
		self.game = game
		self.screen_width = 1200
		self.screen_height = 720

	def new_level(self):
		self.place_hole()
		self.place_ball()
		self.place_magnet()

	def place_hole(self):
		#placement limits
		max_x = self.screen_width - self.game.hole.width
		max_y = self.screen_height - self.game.hole.height
		mid_x = max_x // 2

		#random placement
		self.game.hole.x = random.randint(mid_x + self.game.hole.width
			, max_x)
		self.game.hole.y = random.randint(0, max_y)

	def place_ball(self):
		max_x = self.screen_width - self.game.ball.width
		max_y = self.screen_height - self.game.ball.height
		mid_x = max_x // 2

		#random placement
		for _ in range(100):
			self.game.ball.x = random.randint(0, mid_x)
			self.game.ball.y = random.randint(0, max_y)

			distance = self.game.hole.x - self.game.ball.x

			if distance >= 450:
				break

	def place_magnet(self):
		max_x = self.screen_width - self.game.magnet.width
		max_y = self.screen_height - self.game.magnet.height

		ball_rect = QRect(
			self.game.ball.x,
			self.game.ball.y,
			self.game.ball.width,
			self.game.ball.height
		)

		hole_rect = QRect(
			self.game.hole.x,
			self.game.hole.y,
			self.game.hole.width,
			self.game.hole.height
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