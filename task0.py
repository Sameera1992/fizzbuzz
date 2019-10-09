def buzzfizz():
	print("\n Multiples of 3 and 5 replaced with respective words as peer the program: \n")
	for i in range(101):
		if (i%3 == 0) and (i%5 == 0):
			print("FizzBuzz")
		elif i%3 == 0:
			print("Fizz")
		elif i%5 == 0:
			print("Buzz")
		
		else:
			print(i)
buzzfizz()

