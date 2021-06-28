from gpiozero import Button
import RPi.GPIO as GPIO
from enum import Enum
from utils.actions import Action

button = Button(17)
button2 = Button(27)

GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

class PiController:
	def getActions(self):
		Up = GPIO.input(5)
		Down = GPIO.input(6)
		Right = not button.is_pressed
		Left = not button2.is_pressed

		actions = []

		if GPIO.input(5):
			actions.append(Action.UP)
		if GPIO.input(6):
			actions.append(Action.DOWN)
		if not button.is_pressed:
			actions.append(Action.Right)
		if not button2.is_pressed:
			actions.append(Action.Left)

		return actions
