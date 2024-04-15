#it is clearly seen that self and obj is referring to the same object
# self represents the instance of the class. By using the “self” 
#  we can access the attributes
# and methods of the class in python. It binds the attributes with the given arguments.

# The reason you need to use self. is because Python does not use the @ syntax to refer 
# to instance attributes. 


class check:
	def __init__(self):
		print("Address of self = ",id(self))

obj = check()
obj1 = check()
print("Address of class object = ",id(obj))
print("Address of class object = ",id(obj1))


# this code is Contributed by Samyak Jain
