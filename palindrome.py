def palindrome(s):
	print s[::-1]
	if s[:]==s[::-1]:
		return True
	else:
		return False
print palindrome('mooom')