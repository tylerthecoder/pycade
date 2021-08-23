

def limitValue(val: float, lower: float, upper: float):
	if val > upper:
		return upper
	if val < lower:
		return lower
	return val