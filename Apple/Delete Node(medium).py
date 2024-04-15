


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
	   # goal : delete node 2.
		
        1  ->  2 -> 3       -> 4
               ^    ^
               |    |
              node  node.next
         #step one:  change the node value to 3
         1  ->  3   3           4
               ^    ^           ^
               |    |           |
              node  node.next   node.next.next
              
          #step two: change the next pointer to point to node.next.next
         1  ->  3   ->          4
               ^    ^           ^
               |    |           |
              node  node.next   node.next.next
			  
	    1 ->3 ->4
        """
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
		
class Node:

	# Function to initialise the node object
	def __init__(self, data):
		self.data = data # Assign data
		self.next = None # Initialize next as null
		
class LinkedList:
	# Function to initialize head
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" -> ")
            temp = temp.next
        print()	
            
    def deleteNode(self, node):
        if node.next is None:
            node = None
            return
        node.data = node.next.data
        node.next = node.next.next
    # push function to add node in front of llist
        
    def push(self, new_data):
        # Allocate the Node &
        # Put in the data
        new_node = Node(new_data)
        # Make next of new Node as head
        new_node.next = self.head
        # Move the head to point to new Node
        self.head = new_node
	
    
	#  2-> 4 -> 3 -> 5 
if __name__ == '__main__':
    llist1 = LinkedList()
    # llist2 = LinkedList()
    llist1.push(2)
    llist1.push(4)
    llist1.push(3)
    llist1.push(5)
    print(" Before Deleting ------------")
    print(llist1.printList())
    llist1.deleteNode(llist1.head.next)
    print("After Deleting --------------")
    print(llist1.printList())