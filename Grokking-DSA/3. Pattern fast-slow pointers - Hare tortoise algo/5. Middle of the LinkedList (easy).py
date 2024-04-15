# Problem Statement #
# Given the head of a Singly LinkedList, write a method to return 
# the middle node of the LinkedList.

# If the total number of nodes in the LinkedList is even, return the second middle node.


# Example 1:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> null
# Output: 3

# Example 2:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null
# Output: 4

# Example 3:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> null
# Output: 4


# Approach:
# We can use the Fast & Slow pointers method such that the fast pointer is 
# always twice the nodes ahead of the slow pointer. This way, when the fast pointer 
# reaches the end of the LinkedList, the slow pointer will be pointing at the middle node.

class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end= "")
            temp = temp.next
        print() 

def find_middle_linked_list(head): 
    #  Floyd's Cycle Detection Algorithm.
    # With Floyd's, we'll travel through the linked list with two pointers, 
    # one of which is moving twice as fast as the other. When the fast pointer 
    # reaches the end of the list, the slow pointer must then be in the middle.
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next    
    return slow  
      
       
def main():
  head =  Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
#   head.next.next.next = Node(4)
#   head.next.next.next.next = Node(5)
#   head.next.next.next.next.next = Node(6)
  head.print_list()
  print("Middle Node: "  + (str(find_middle_linked_list(head).value)))


main()