import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    head = ListNode(None)
    curr = head
    h = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next
    
    while h:
        val, i = heapq.heappop(h)
        curr.next = ListNode(val)
        curr = curr.next
        if lists[i]:
            heapq.heappush(h, (lists[i].val, i))
            lists[i] = lists[i].next
    
    return head.next

# Example usage:

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [
    l1, l2,l3
]
merged_list = mergeKLists(lists)

# Print the merged list
while merged_list:
    print(merged_list.val, end="->")
    merged_list = merged_list.next
