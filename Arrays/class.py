class Car:
	
	# Class Variable
	vehicle = 'Car'		
	
	# The init method or constructor
	def __init__(self, model, price):
	
		# Instance Variable	
		self.model = model
		self.price = price		
	
# Objects of class
Audi = Car("R8", 100000)
BMW = Car("I8", 10000000)

print('Audi details:')
print('Audi is a', Audi.vehicle)
print('Model: ', Audi.model)
print('price: ', Audi.price)

print('\n BMW details:')
print('BMW is a', BMW.vehicle)
print('Model: ', BMW.model)
print('Color: ', BMW.price)

# Class variables can be
# accessed using class
# name also
print("\nAccessing class variable using class name")
print(Car.vehicle)

# or
print(Audi.vehicle)

# or
print(BMW.vehicle)
