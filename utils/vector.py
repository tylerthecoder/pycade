from __future__ import annotations
from typing import Union, Tuple
import math


class Vector():
	x = 0
	y = 0

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

	def addX(self, val: int):
		x = self.x + val
		return Vector(x, self.y)

	def addY(self, val: int):
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

	def copy(self):
		return Vector(self.x, self.y)

	def getTuple(self):
		return (self.x, self.y)

def VectorLikeToVector(v: Union[Vector, Tuple]):
	if isinstance(v, Vector):
		return v
	elif isinstance(v, tuple):
		return Vector(v)
	else:
		raise Exception(f'Unsupported type: {type(v)}')








