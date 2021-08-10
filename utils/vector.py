from __future__ import annotations
from typing import Union, Tuple
import math

class Vector():
	x: float = 0
	y: float = 0

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return f'{self.x},{self.y}'

	def __eq__(self, value):
		return self.x == value.x and self.y == value.y

	def add(self, val: Vector):
		x = self.x + val.x
		y = self.y + val.y
		return Vector(x, y)

	def addX(self, val: float):
		x = self.x + val
		return Vector(x, self.y)

	def addY(self, val: float):
		y = self.y + val
		return Vector(self.x, y)

	def distance(self, val: Vector):
		return math.sqrt((self.x - val.x) ** 2 + (self.y - val.y) ** 2)

	def scalarMultiply(self, val: float):
		x = self.x * val
		y = self.y * val
		return Vector(x, y)

	def sub(self, val: Vector):
		x = self.x - val.x
		y = self.y - val.y
		return Vector(x, y)

	def constrain(self, lowerValue: Vector, upperValue: Vector):
		x = upperValue.x if self.x > upperValue.x else lowerValue.x if self.x < lowerValue.x else self.x
		y = upperValue.y if self.y > upperValue.y else lowerValue.y if self.y < lowerValue.y else self.y
		return Vector(x, y)

	def copy(self):
		return Vector(self.x, self.y)

	def getTuple(self):
		return (self.x, self.y)

def VectorLikeToVector(v: Union[Vector, Tuple]):
	if isinstance(v, Vector):
		return v
	elif isinstance(v, tuple):
		return Vector(v[0], v[1])
	else:
		raise Exception(f'Unsupported type: {type(v)}')








