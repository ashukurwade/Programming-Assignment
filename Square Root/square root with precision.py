def findsqrt(number, precision):
    
	s = 0
	e, root = number, 1
	
	while (s <= e):
		m = int((s + e) / 2)

		if (m * m == number):
			root = m
			break
			
		if (m * m < number):
			s = m + 1
			root = m
			
		else:
			e = m - 1

	incr = 0.1
	for i in range(0, precision):
		while (root * root <= number):
			root += incr
			
		root = root - incr
		incr = incr / 10

	return root

print(round(findsqrt(35, 3), 4))