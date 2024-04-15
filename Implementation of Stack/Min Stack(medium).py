# Design a stack that supports push, pop, top, and retrieving the
#  minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


class MinStack:
    # def __init__(self):
    #     """
    #     initialize your data structure here.
    #     """
    #     self.stack = []
    #     self.currentMin = float('inf')
    #     self.prevMins = []
        
    # def push(self, x: int) -> None:
    #     self.stack.append(x)
    #     if x <= self.currentMin:
    #         self.prevMins.append(self.currentMin)
    #         self.currentMin = x

    # def pop(self) -> None:
    #     if self.stack[-1] == self.currentMin:
    #         self.currentMin = self.prevMins.pop()
    #     self.stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.currentMin

    def __init__(self):
        self.A = []
        self.M = []

    def push(self, x):
        self.A.append(x)
        self.M.append( x if not self.M else min(x, self.M[-1]) )

    def pop(self):
        self.A.pop()
        self.M.pop()

    def top(self):
        return self.A[-1]

    def getMin(self):
        return self.M[-1]

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
print("push")
minStack.push(0)
print(minStack.stack)
print("push")
minStack.push(-3)
print(minStack.stack)
print("getMin")
print(minStack.getMin()) # return -3
print("pop")
minStack.pop()
print(minStack.stack)
print("top")
print(minStack.top())    # return 0
print("getMin")
print(minStack.getMin()) # return -2      

