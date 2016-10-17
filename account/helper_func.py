from random import sample
from string import digits, ascii_letters

def rand_name():
	name = ''.join(sample(ascii_letters, 4))+''.join(sample(digits, 2))
	return name
