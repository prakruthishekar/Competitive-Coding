# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
# Your code will be tested with the following pseudocode:

# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#     append iterator.next() to the end of res
# return res
# If res matches the expected flattened list, then your code will be 
# judged as correct.

 

# Example 1:

# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false,
# the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:

# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, 
# the order of elements returned by next should be: [1,4,6].


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


# using recursion
class NestedIterator:
    def __init__(self, nestedList):
        def flatten(nested):
            result = []
            for ni in nested:
                if isinstance(ni,int):
                    result.append(ni)
                else:
                    result.extend(flatten(ni))
            return result
        
        self.flattened = flatten(nestedList)
        self.index = 0

    def next(self) -> int:
        self.index += 1
        return self.flattened[self.index - 1]

    def hasNext(self) -> bool:
        return self.index < len(self.flattened)
            



# # Using stack
# class NestedIterator:
#     def __init__(self, nestedList):
#         self.stack = nestedList[::-1]
    
#     def next(self) -> int:
#         return self.stack.pop().getInteger()
    
#     def hasNext(self) -> bool:
#         while self.stack:
#             top = self.stack[-1]
#             if top.isInteger():
#                 return True
#             self.stack = self.stack[:-1] + top.getList()[::-1]
#         return False
    

# Your NestedIterator object will be instantiated and called as such:
# Assuming you have defined the NestedIterator class as mentioned earlier

# Initialize the iterator with nestedList
nestedList = [[1, 1], 2, [1, 1]]
iterator = NestedIterator(nestedList)

# Initialize an empty list to store the flattened elements
res = []

# Iterate through the iterator until there are no more integers left
while iterator.hasNext():
    # Append the next integer returned by next() to the end of res
    res.append(iterator.next())

# Return the flattened list
print(res)



# Time complexity:

# Flattening or processing the list is O(N), where NNN is the total number of integers 
# in the nested structure. We handle each integer only once.
# Both next and hasNext operations are O(1) on average. Though there might be cases in 
# the stack approach where hasNext takes longer, over a series of operations, it averages out 
# to O(1)


# Space complexity:

# The maximum space required is O(N). This is because of the flattened list in the 
# recursive approach or due to the stack in the stack approach.