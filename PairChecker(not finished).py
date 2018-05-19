def pair_checker(ntch,n1,n2,n3,n4):
	numbers = [n1,n2,n3,n4]
	i = 0
	low = 0
	high = 1
	result = numbers[low]+numbers[high] 
	while i < len(numbers)*4:
		
		if result == ntch:
			print str(numbers[low])+" + "+str(numbers[high])
		high += 1
		if high == 3:
			low += 1
			high = 0
		

pair_checker(8,4,4,2,6)



