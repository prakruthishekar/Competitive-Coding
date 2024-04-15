# Palindrome LinkedList (medium) #
# Given the head of a Singly LinkedList, write a method to check if the LinkedList is 
# a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the 
# original form once the algorithm is finished. The algorithm should have O(N)O(N) time 
# complexity where ‘N’ is the number of nodes in the LinkedList.


# Example 1:

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true
# Example 2:

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false



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



# Naive Approach
# Store nodes to an array and check the array elements 
# if the first elements and last elements are similar

# def isPalindrome(head):
#     pointer = head
#     arr = []
#     while pointer:
#         arr.append(pointer.value)
#         pointer = pointer.next
    
#     n = len(arr)
#     for i in range(n//2):
#         if arr[i] != arr[n-1-i]:
#             return False
#     return True




# Solution 

# We can use the Fast & Slow pointers method similar to Middle of the 
# LinkedList to find the middle node of the LinkedList.

# Once we have the middle of the LinkedList, we will reverse the second half.

# Then, we will compare the first half with the reversed second half to see 
# if the LinkedList represents a palindrome.

# Finally, we will reverse the second half of the LinkedList again to revert 
# and bring the LinkedList back to its original form.



def isPalindrome(head):

    #find middle of the linkedList
    slow, fast = head, head
    while(fast and fast.next):
        slow = slow.next
        fast = fast.next.next

    head_second_half = reverse(slow) # reverse the second half
    #store the head of the reversed part to revert back later

    copy_head_second_half = head_second_half

    while(head and head_second_half):
        if (head.value != head_second_half.value):
            break # not a palindrome
        head = head.next
        head_second_half = head_second_half.next

    reverse(copy_head_second_half) # reverse the reverse of the second half

    if(head is None and head_second_half is None): # if both halves match
        return True
    return False

def reverse(head):
    prev = None
    while(head):
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev 




# # this is just checking if it's palindrome or not, but the linked list will be distorted
# def isPalindrome(head):
#     #find middle of the linkedList
#         slow, fast = head, head
#         while(fast and fast.next):
#             slow = slow.next
#             fast = fast.next.next

#         # reverse the second half
#         prev = None
#         while(head):
#             temp = head.next
#             head.next = prev
#             prev = head
#             head = temp

#         #check palindrome
#         while(head and prev):
#             if (head.val != prev.val):
#                 return False # not a palindrome
#             head = head.next
#             prev = prev.next
        
#         return True



  
def main():
  head =  Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)
  print("Is Palindrome: "  + str(isPalindrome(head)))
  head.print_list()
#   head.next.next.next.next.next = Node(6)
#   print("Is Palindrome: "  + str(isPalindrome(head)))

main()