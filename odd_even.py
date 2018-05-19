num = int(raw_input('put a number over here : '))
def num_checker(n):
	if n % 2 == 0 :
		print 'This number is even!'
	if n % 2 != 0 :
		print 'This number is odd!'
	if n % 2 == 0 and  n % 4 == 0 :
	    print 'And this number is devided by 4 too !! ' 

num_checker(num)