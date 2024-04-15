# Using List
# - easy to implememt
# - Speed problem when it grows as memory allocation 
# is required since values are stored beside each other 


# Creting stack using list without the size limit
class Stack:
    def __init__(self) -> None:
        self.list = []        #Time and Space = O(1)
        
        
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

    # push
    def push(self, value):
        self.list.append(value) 
        return "The element has been successfully inserted"

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


    # delete 
    def delete(self):
        self.list = None         


custonStack = Stack()
custonStack.push(2)
custonStack.push(1)                 
custonStack.push(4)                 
custonStack.push(5)
 
print(custonStack.pop())
print(custonStack.peek())
print(custonStack)
print(custonStack)




