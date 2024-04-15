# Rearrange a LinkedList (medium) #
# Given the head of a Singly LinkedList, write a method to modify the 
# LinkedList such that the nodes from the second half of the LinkedList are 
# inserted alternately to the nodes from the first half in reverse order.
# So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, 
# your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList 
# should be modified in-place.

# Example 1:

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 
# Example 2:

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
# Output: 2 -> 10 -> 4 -> 8 -> 6 -> null


class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end= " ")
            temp = temp.next
        print() 








# Using Stack
# def reorderList(head) -> None:
#         """
#         Do not return anything, modify head in-place instead.
#         """
#         if not head:
#             return
#         stack =[]
#         node = head
#         while node:
#             stack.append(node)
#             node = node.next
#         node = head
#         for i in range(len(stack)//2):
#             last = stack.pop()
#             nextElement = node.next
#             node.next = last
#             last.next = nextElement
#             node = nextElement
#         node.next = None





def reorderList(head):

    #find middle of the linkedList
    slow, fast = head, head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow) # reverse the second half
    #store the head of the reversed part to revert back later

    head_first_half = head

    while(head_first_half is not None and head_second_half is not None):
        temp = head_first_half.next
        head_first_half.next = head_second_half
        head_first_half = temp

        temp = head_second_half.next
        head_second_half.next = head_first_half
        head_second_half = temp
    

    if head_first_half is not None:
        head_first_half.next = head

def reverse(head):
    prev = None
    while(head):
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev 


def main():
  head =  Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print(reorderList(head))
  head.print_list()

main()