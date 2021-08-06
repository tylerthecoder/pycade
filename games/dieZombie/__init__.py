from games.games import PycadeGame

# This is going to be a 2D "dungeon crawler" game where you fight zombies in each room
# There are differnet weapons and powerups that you pick up


class DieZombie(PycadeGame):
	def start(self):
		pass

	@staticmethod
	def get_name():
		return "Die Zombie"

	def update(self):
		return True

	def draw(self):
		self.drawText("Tyler", (0, 0))

