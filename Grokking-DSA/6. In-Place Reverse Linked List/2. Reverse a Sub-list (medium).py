# Given the head of a singly linked list and two integers left and
# right where left <= right, reverse the nodes of the list from position
# left to position right, and return the reversed list.

 

# Example 1:


# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [5], left = 1, right = 1
# Output: [5]


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




# Skip the first p-1 nodes, to reach the node at position p.

# Remember the node at position p-1 to be used later to connect
# with the reversed sub-list.

# Next, reverse the nodes from p to q using the same approach 
# discussed in Reverse a LinkedList.

# Connect the p-1 and q+1 nodes to the reversed sub-list.

def reverse_sub_list(head, left, right):
    # Comparing with Problem 206: just need to find the start position 
    # then reverse (same as 206)
    
    dummy = Node(0)
    dummy.next = head
    
    pre = dummy
    cur = dummy.next
    
    # find the position
    for i in range(1,left):
        cur = cur.next
        pre = pre.next
    
    # next_node = head.next # temporarily store the next node
    # head.next = prev # reverse the current node
    # prev = head # before moving to next node, point previous to current node
    # head = next_node 
    # reverse
    
    for i in range(right-left):
        # 1->2->3->4->5->6
        temp = cur.next # temp = (3) temporarily store cur.next node 
        cur.next = temp.next # 1->2->4->5->6
        temp.next  = pre.next # 3->2
        pre.next = temp # 1->3
    
    return dummy.next
    
       
def main():
  head =  Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
#   head.next.next.next.next.next.next = Node(7)
#   head.next.next.next.next.next.next.next = Node(8)  
  print("Nodes of Original Linked List are ", end="")
  head.print_list()
  result = reverse_sub_list(head,2,4)
  print("Nodes of reversed linked List are ", end="")
  result.print_list()

main()
