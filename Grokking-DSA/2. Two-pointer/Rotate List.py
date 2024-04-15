
# Rotate List

# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]
# Example 2:


# Input: head = [0,1,2], k = 4
# Output: [2,0,1]


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

def rotateRight(head, k):
    if not head:
        return None

    lastElement = head
    length = 1
    # get the length of the list and the last node in the list
    while ( lastElement.next ):
        lastElement = lastElement.next
        length += 1

    # If k is equal to the length of the list then k == 0
    # ElIf k is greater than the length of the list then k = k % length
    k = k % length
        
    # Set the last node to point to head node
    # The list is now a circular linked list with last node pointing to first node
    lastElement.next = head
    
    # Traverse the list to get to the node just before the ( length - k )th node.
    # Example: In 1->2->3->4->5, and k = 2
    #          we need to get to the Node(3)
    tempNode = head
    for _ in range( length - k - 1 ):
        tempNode = tempNode.next
    
    # Get the next node from the tempNode and then set the tempNode.next as None
    # Example: In 1->2->3->4->5, and k = 2
    #          tempNode = Node(3)
    #          answer = Node(3).next => Node(4)
    #          Node(3).next = None ( cut the linked list from here )
    answer = tempNode.next
    tempNode.next = None
    
    return answer
		
			
    
# Use push() to construct below
# list 1-> 12-> 1-> 4-> 1
if __name__ == '__main__':
	llist1 = LinkedList()
	llist2 = LinkedList()
	llist1.append(2)
	llist1.append(4)
	llist1.append(3)
	llist1.append(5)
	llist1.append(6)
	llist1.printList()
	val = rotateRight(llist1.head,k = 2)

    # llist1.printList()

