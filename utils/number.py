

def limitValue(val: int, lower: int, upper: int):
	if val > upper:
		return upper
	if val < lower:
		return lower
	return val