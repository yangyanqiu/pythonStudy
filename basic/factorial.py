def factorial(n):
	if n > 1 :
		n = n * factorial(n-1)
	elif n == 0 or n == 1:
		n = 1
	return n

def main():
	print "Please enter a int number to get it's factorial:"
        try:
		number = int(raw_input())
		if number < 0:
			print str(number) + " has no factorial."
		else:
			factorialN = factorial(number)
			print str(number) + "'s factorial is " + str(factorialN)
	except Exception as e:
		print e 
		print "You cannot enter a charactor, and you should enter a number."
	

if __name__ == "__main__":
	main()
		
         
		
