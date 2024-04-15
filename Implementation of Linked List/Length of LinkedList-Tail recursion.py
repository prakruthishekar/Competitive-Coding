# A complete working Python3 program to find length of a
# Linked List using Tail recursion.

# Node class


class Node:
	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# This function is in LinkedList class. It inserts
	# a new node at the beginning of Linked List.

	def push(self, new_data):

		# 1 & 2: Allocate the Node &
		#	 Put in the data
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		new_node.next = self.head

		# 4. Move the head to point to new Node
		self.head = new_node

	# This function counts number of nodes in Linked List
	# recursively, given 'node' as starting node using Tail Recursion.
	def getCountRec(self, node, count=0):
		if (not node): # Base case
			return count
		else:
			return self.getCountRec(node.next, count+1)

	# A wrapper over getCountRec()
	def getCount(self):
		return self.getCountRec(self.head)


# Driver code
if __name__ == '__main__':
	llist = LinkedList()
	llist.push(1)
	llist.push(3)
	llist.push(1)
	llist.push(2)
	llist.push(1)
	
	# Function call
	print('Count of nodes is :', llist.getCount())

	# This code is contributed by garinesrija.
# Time Complexity: O(N), As we are traversing the list only once.
# Auxiliary Space: O(1), As we are using the tail recursive function, 
# no extra space is used in the function call stack.