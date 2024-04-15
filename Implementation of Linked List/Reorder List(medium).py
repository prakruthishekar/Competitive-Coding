





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
			
# def reorderList(head) -> None:
    # if not head:
    #     return
    # stack =[]
    # node = head
    # while node:
    #     stack.append(node)
    #     node = node.next
    # node = head
    # for i in range(len(stack)//2):
    #     last = stack.pop()
    #     nextElement = node.next
    #     node.next = last
    #     last.next = nextElement
    #     node = nextElement
    # node.next = None



def reorderList(head) -> None:
    # divide the linked list
    slow,fast=head,head.next
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    second=slow.next
    # making Null of half linked list
    prev=slow.next=None
    # reverse the end linked list
    while second:   
        nxt=second.next
        second.next=prev
        prev=second
        second=nxt
    # merging the divided linked list
    first,last=head,prev
    while last:
        nxt1,nxt2=first.next,last.next
        first.next=last
        last.next=nxt1
        first,last=nxt1,nxt2
        

# Code execution starts here
if __name__=='__main__':

	# Start with the empty list
	llist = LinkedList()
	# Insert 6. So linked list becomes 6->None
	llist.append(1)
	llist.append(2)
	llist.append(3)
	llist.append(4)   
	llist.printList() 
	reorderList(llist.head)
	llist.printList()