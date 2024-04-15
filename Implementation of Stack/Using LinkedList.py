# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, value = None):
		self.value = value # Assign data
		self.next = next # Initialize next as null - it's the location


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None