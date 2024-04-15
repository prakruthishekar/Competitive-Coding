# Given the head of a linked list, reverse the nodes of the list k at a time, 
# and return the modified list.

# k is a positive integer and is less than or equal to the length of the
# linked list. If the number of nodes is not a multiple of k then left-out nodes, 
# in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves 
# may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]

class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end="")
            if temp.next is not None:
                print("->", end="")  # Print "->" only if there is a next node
            temp = temp.next
        print()


def reverseKGroup(head, k: int):
         # Check if we need to reverse the group
        curr = head
        for _ in range(k):
            if not curr: return head
            curr = curr.next
		        
        # Reverse the group (basic way to reverse linked list)
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # After reverse, we know that `head` is the tail of the group.
		# And `curr` is the next pointer in original linked list order
        head.next = reverseKGroup(curr, k)
        return prev    
        

def main():
  head =  Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)


  
  print("Nodes of Original Linked List are ", end="")
  head.print_list()
  result = reverseKGroup(head, 3)
  print("Nodes of reversed linked List are ", end="")
  result.print_list()


main()
