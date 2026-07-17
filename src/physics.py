#physics.py

def boundary_collision(game_object, game):

	game_object.x = max(
		0,
		min(game_object.x, game.width() - game_object.width)
	)

	game_object.y = max(
		0,
		min(game_object.y, game.height() - game_object.height)
	)