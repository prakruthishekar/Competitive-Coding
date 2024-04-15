# # 

# # Example 1
# # Input: head = [1,2,3,4,5], n = 2
# # Output: [1,2,3,5]
# # Example 2:

# # Input: head = [1], n = 1
# # Output: []
   

# Take two pointers – fast and slow. And initialize their values as head node
# Iterate fast pointer till the value of n.
# Now, start iteration of fast pointer till the None value of the linked list. Also, iterate slow pointer.
# Hence, once the fast pointer will reach to the end the slow pointer will reach the node 
# which you want to delete.

# Replace the next node of the slow pointer with the next to next node of the slow pointer.
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def display(self):
		temp = self.head
		while temp != None:
			print(temp.data)
			temp = temp.next

	def deleteNthNodeFromEnd(self, head, n):
		fast = head
		slow = head

		for _ in range(n):
			fast = fast.next

		if not fast:
			return head.next

		while fast.next:
			fast = fast.next
			slow = slow.next

		slow.next = slow.next.next
		return head


if __name__ == '__main__':
	l = LinkedList()
	l.push(5)
	l.push(4)
	l.push(3)
	l.push(2)
	l.push(1)
	print('***** Linked List Before deletion *****')
	l.display()

	print('************** Delete nth Node from the End *****')
	l.deleteNthNodeFromEnd(l.head, 2)

	print('*********** Linked List after Deletion *****')
	l.display()