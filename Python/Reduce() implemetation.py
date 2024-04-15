# Reduce function i.e. reduce() function works with 3 parameters in 
# python3 as well as for 2 parameters. To put it in a simple way reduce() 
# places the 3rd parameter before the value of the second one, if it’s present.
#  Thus, it means that if the 2nd argument is an empty sequence, then 3rd 
#  argument serves as the default one. 

# Python program to illustrate sum of two numbers.
def reduce(function, iterable, initializer=None):
	it = iter(iterable)
	if initializer is None:
		value = next(it)
	else:
		value = initializer
	for element in it:
		value = function(value, element)
	return value

# Note that the initializer, when not None, is used as the first value instead of the first value from iterable , and after the whole iterable.
tup = (2,1,0,2,2,0,0,2)
print(reduce(lambda x, y: x+y, tup,6))

# This code is contributed by aashutoshjha
