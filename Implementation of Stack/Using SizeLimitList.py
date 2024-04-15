# Stack using Linked list
# - fask Performance
# - Implementation is not easy

class Stack:
    def __init__(self, maxSize) -> None:
        self.list = []        #Time and Space = O(1)
        self.maxSize = maxSize
        
        
    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)


    # isEmpty                #Time and Space = O(1)
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False  

    # isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    # pop
    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list.pop() 

    # peek
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.list[len(self.list) - 1] 

    def push(self, value):
        if self.isFull():
            return "The stack is full"

        else:
            self.list.append(value)  

custonStack = Stack(4)
print(custonStack.isEmpty())
custonStack.push(2)
custonStack.push(1)                 
custonStack.push(4)                 
custonStack.push(5)
 
print(custonStack.pop())
print(custonStack.peek())
print(custonStack)                  
