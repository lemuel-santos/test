def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

def test_subtract():
	assert subtract(3, 1) == 2

def test_addition():
	assert add(3, 1) == 5
