import random
def overlap():
	list1=random.sample(range(50), 15)
	list2=random.sample(range(50), 15)
	result=[]
	for element in list1:
		if element in list2:
			if element in result:
				print ("the element ["+str(element)+"] exist more than once")
			else:
			    result.append(element)
	print "These are the elements that are common between the lists "+str(result)


overlap()