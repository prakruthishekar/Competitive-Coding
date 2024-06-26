class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # create a dummy node to hold the merged list
    dummy = ListNode(-1)
    curr = dummy
    
    # traverse both lists and merge the nodes in sorted order
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    # append the remaining nodes in one of the lists, if any
    curr.next = l1 if l1 else l2
    
    # return the merged list
    return dummy.next



# create two sorted linked lists
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))

# call the mergeTwoLists function to merge the two lists
merged = mergeTwoLists(l1, l2)

# print the merged list
while merged:
    print(merged.val, end=" ")
    merged = merged.next
