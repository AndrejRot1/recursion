def fractions(n):
	if n == 1:
		return 1
	else:
		return n * fractions(n-1)

