a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = input('Type a number')
def less_than(x):
	list = [y for y in a if y<x]
	return list
print less_than(n)