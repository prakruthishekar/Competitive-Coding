# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single
# digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except
# the number 0 itself.

 

# Example 1:

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]




class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null
		
class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None
			    
	# push function to add node in front of llist
	def push(self, new_data):
		# Allocate the Node &
		# Put in the data
		new_node = Node(new_data)
		# Make next of new Node as head
		new_node.next = self.head
		# Move the head to point to new Node
		self.head = new_node
		
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

	def printList(self):
		temp = self.head
		while (temp):
			print(temp.data,end=" ")
			temp = temp.next
		print()	

def addTwoNumber(l1,l2):
	dummy = cur = Node(0)
	carry = 0
	while l1 or l2 or carry:
		if l1:
			carry += l1.data
			l1 = l1.next
		if l2:
			carry += l2.data
			l2 = l2.next
		cur.next = Node(carry%10)
		cur = cur.next
		carry //=10
	return dummy.next
		
			
    
# Use push() to construct below
# list 1-> 12-> 1-> 4-> 1
if __name__ == '__main__':
	llist1 = LinkedList()
	llist2 = LinkedList()
	llist1.append(2)
	llist1.append(4)
	llist1.append(3)
	llist2.append(5)
	llist2.append(6)
	llist2.append(4)

	llist1.printList()
	llist2.printList()
	val = addTwoNumber(llist1.head,llist2.head)

	while(val):
		print(val.data, end='')
		val = val.next
	
	



	

# Time Complexity: O(n) 
# Auxiliary Space: O(1)
