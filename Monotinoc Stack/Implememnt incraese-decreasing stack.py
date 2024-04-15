# Python code to implement the approach

# Function to build Monotonic increasing stack
def increasingStack(arr):
	# Initialise stack
	stk=[]
	
	for i in range(len(arr)):
		# Either stack is empty or
		# all bigger nums are popped off
		while(len(stk) > 0 and stk[len(stk) - 1] > arr[i]):
			stk.pop()
		stk.append(arr[i])
		
	return stk

def decreasingStack(arr):
	# Initialise stack
	stk=[]
	
	for i in range(len(arr)):
		# Either stack is empty or
		# all bigger nums are popped off
		while(len(stk) > 0 and stk[len(stk) - 1] < arr[i]):
			stk.pop()
		stk.append(arr[i])
		
	return stk
	

# Function Call
print(increasingStack([1, 4, 5, 3, 12, 10]))
print(decreasingStack([15, 17, 12, 13, 14, 10 ]))


# This code is contributed by Pushpesh Raj.
