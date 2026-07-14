# level.py
import random
import math


class Level:

	def __init__(self, game):
		self.game = game

	def new_level(self):
		self.place_hole()
		self.place_ball()

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
