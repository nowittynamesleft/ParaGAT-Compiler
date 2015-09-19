def lexer(s):
	words = s.split(' ')
	for word in words:
		yield word

if __name__ -== '__main__':
	s = "abc def x + 17"
	for w in lexer(s):
		print w

# HINT: Install anaconda python
# HINT: Learn python 3, not python 2
# NOTE: above code might be in python 2, not 3