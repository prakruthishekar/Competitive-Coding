# Problem Statement #
# Given the head of a Singly LinkedList that contains a cycle, 
# write a function to find the starting node of the cycle.



# Approach

# Take two pointers. Let’s call them pointer1 and pointer2.

# Initialize both pointers to point to the start of the LinkedList.

# We can find the length of the LinkedList cycle using the approach discussed in 
# LinkedList Cycle. Let’s assume that the length of the cycle is ‘K’ nodes.

# Move pointer2 ahead by ‘K’ nodes.

# Now, keep incrementing pointer1 and pointer2 until they both meet.

# As pointer2 is ‘K’ nodes ahead of pointer1, which means, pointer2 must have completed one 
# loop in the cycle when both pointers meet. Their meeting point will be the start of the cycle.

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

def find_cycle_start(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # found cycle
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
       
def main():
  head =  Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = head.next


  print("Linked List cycle start: " + str(find_cycle_start(head).value))
main()  