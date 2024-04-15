
# Example 1:


# Input: head = [1,3,4,7,1,2,6]
# Output: [1,3,4,1,2,6]
# Explanation:
# The above figure represents the given linked list. 
# The indices of the nodes are written below.
# Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
# We return the new list after removing this node. 
# Example 2:


# Input: head = [1,2,3,4]
# Output: [1,2,4]
# Explanation:
# The above figure represents the given linked list.
# For n = 4, node 2 with value 3 is the middle node, which is marked in red.




class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Constructor to initialize the node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def deleteList(self):
        # Initialize the current node
        current = self.head
        while current:
            next_to_current = current.next  # Move to the next node
            # Delete the current node
            del current.data
            # Set current to the next node
            current = next_to_current

        # In Python, garbage collection happens
        # Therefore, setting self.head = None
        # would also delete the linked list

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end="")
            temp = temp.next
            if temp:  # Check if there is a next element
                print("->", end="")
        print()

    # Push function to add a node at the front of the linked list
    def push(self, new_data):

        # Allocate the Node &
        # Put in the data
        new_node = Node(new_data)

        # Make the next of the new Node as head
        new_node.next = self.head

        # Move the head to point to the new Node
        self.head = new_node


def deleteMiddleElement(head):
    if not head.next:
        return head.next

    fast, slow = head.next.next, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    slow.next = slow.next.next
    return head


# Use push() to construct the linked list: 1->3->4->7->1->2->6
if __name__ == '__main__':

    llist = LinkedList()
    llist.push(1)
    llist.push(3)
    llist.push(4)
    llist.push(7)
    llist.push(1)
    llist.push(2)
    llist.push(6)

    print("Original linked list:")
    llist.printList()

    # Delete the middle element
    deleteMiddleElement(llist.head)

    print("Linked list after deleting the middle element:")
    llist.printList()
