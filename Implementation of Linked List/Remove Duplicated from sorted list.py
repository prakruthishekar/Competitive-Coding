# A complete working Python program to demonstrate all
# insertion methods of linked list

# Node class
class Node:

	# Function to initialise the node object
	def __init__(self, data=0):
		self.data = data # Assign data
		self.next = None # Initialize next as null - it's the location


# Linked List class contains a Node object
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None


	# Function to insert a new node at the beginning
	def push(self, new_data):

		# 1 & 2: Allocate the Node &
		#	 Put in the data
		new_node = Node(new_data)

		# 3. Make next of new Node as head
		# this will assign the address of head to new_node
		new_node.next = self.head 
		# 4. Move the head to point to new Node
		# this will assign the address of new_node which is None to head
		self.head = new_node


	# This function is in LinkedList class. Inserts a
	# new node after the given prev_node. This method is
	# defined inside LinkedList class shown above */
	def insertAfter(self, prev_node, new_data):

		# 1. check if the given prev_node exists
		if prev_node is None:
			print("The given previous node must be in LinkedList.")
			return

		# 2. create new node &
		#	 Put in the data
		new_node = Node(new_data)

		# 4. Make next of new Node as next of prev_node
		new_node.next = prev_node.next

		# 5. make next of prev_node as new_node
		prev_node.next = new_node


	# This function is defined in Linked List class
	# Appends a new node at the end. This method is
	# defined inside LinkedList class shown above */
	def append(self, new_data):

		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
		new_node = Node(new_data)

		# 4. If the Linked List is empty, then make the
		# new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# 6. Change the next of last node
		last.next = new_node


	# Utility function to print the linked list
	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data,end=" ")
			temp = temp.next

	def deleteDuplicates(self, head):
		cur = head
		while cur:
			if cur.next and cur.next.data == cur.data:
				cur.next = cur.next.next
			else:
				cur = cur.next
		return head
	

# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
	llist = LinkedList()
	llist1 = LinkedList()

	# Insert 6. So linked list becomes 6->None
	llist.append(1)
	llist.append(1)
	llist.append(3)
	llist.append(5)
	print('Created linked list is: ')
	llist.printList()
	print()
	llist.deleteDuplicates(llist.head)
	print('Reversed linked list is: ')
	llist.printList()


# This code is contributed by Manikantan Narasimhan

# Time Complexity: O(N) 
# Auxiliary Space: O(1)