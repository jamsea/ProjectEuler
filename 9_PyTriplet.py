import math
for x in range(0,1000):
	for y in range(0,1000):
		z = math.sqrt(x**2 + y**2)
		if x + y + z == 1000:
			print x*y*z

	
