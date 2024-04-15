# You are given an array of k linked-lists lists, each linked-list is sorted 
# in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6


# Example 2:

# Input: lists = []
# Output: []

# Example 3:

# Input: lists = [[]]
# Output: []


from ast import List
from pyparsing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            mergedLists = []
            # utilizing merge sort algorithm
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergelist(l1, l2))  
            lists = mergedLists
        return lists[0]

    def mergelist(self, l1: ListNode, l2: ListNode) -> ListNode:
        # create a dummy node to hold the merged list
        dummy = ListNode()
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