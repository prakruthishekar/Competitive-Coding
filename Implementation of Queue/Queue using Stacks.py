# # The problem is opposite of this post. We are given a stack data structure with
# # push and pop operations, the task is to implement a queue using instances of 
# # stack data structure and operations on them.


# Implement a first in first out (FIFO) queue using only two stacks. 
# The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, 
# peek/pop from top, size, and is empty operations are valid.

# Depending on your language, the stack may not be supported natively. 
# You may simulate a stack using a list or deque (double-ended queue) as long as
# you use only a stack's standard operations.



# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.master = []
        self.slave = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while len(self.master):
            top = self.master.pop()
            self.slave.append(top)
        self.master.append(x)
        while len(self.slave):
            top = self.slave.pop()
            self.master.append(top)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.master.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.master[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not len(self.master)
    

myQueue  = MyQueue()
myQueue.push(1) # queue is: [1]
myQueue.push(2) # queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek() # return 1
myQueue.pop() # return 1, queue is [2]
myQueue.empty() # return false