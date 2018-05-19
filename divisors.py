n = input('type a number : ')
def divisors(number):
	i = 1
	
	while i < number:
		if number % i == 0:
			print i

		i+=1
    
divisors(n)
