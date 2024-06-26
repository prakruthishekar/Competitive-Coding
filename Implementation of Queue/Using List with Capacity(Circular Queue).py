#   Created by Elshad Karimov on 29/05/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class Queue:
    def __init__(self, maxSize):
        #In python to create fixed set of elements in array we need to assign None value
        self.items = maxSize * [None] 
        self.maxSize = maxSize
        self.start = -1
        self.top = -1 
    # Time complexity = O(1)
    # Space complexity = O(n)    
    # For enqueue we update the top variable, if top variable reach the end we set it to 0
    # and start updating the value
    # for dequeue we update the start variable
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self): # #Time complexity = O(1)
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def enqueue(self, value): #Time complexity = O(1)
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"
    
    def dequeue(self): #Time complexity = O(1)
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    def peek(self): #Time complexity = O(1)
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
    
    def delete(self): #Time complexity = O(1)
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.dequeue()
customQueue.dequeue()
customQueue.dequeue()
customQueue.dequeue()
customQueue.delete()
print(customQueue)