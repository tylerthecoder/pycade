from pynput.keyboard import Key, Listener
from utils.actions import Action



class KeyboardController:
	nextActions = []

	def __init__(self):
		super().__init__()
		# Collect events until released
		with Listener(
						on_press=self.on_press,
						on_release=self.on_release) as listener:
				listener.join()

	def on_press(self, key):
			print('{0} pressed'.format(
					key))

	def getActionFromKey(self, key):
		if key == key.w:
			return Action.UP
		if key == key.a:
			return Action.LEFT
		if key == key.d:
			return Action.RIGHT
		if key == key.s:
			return Action.DOWN

	def on_release(self, key):
			print('{0} release'.format(
					key))

			action = self.getActionFromKey(key);
			if action:
				self.nextActions.append(action)

			if key == Key.esc:
					# Stop listener
					return False

	def getActions(self):


		nextActions = []







