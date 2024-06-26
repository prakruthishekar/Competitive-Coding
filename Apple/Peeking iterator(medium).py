# Design an iterator that supports the peek operation on an existing iterator
# in addition to the hasNext and the next operations.

# Implement the PeekingIterator class:

# PeekingIterator(Iterator<int> nums) Initializes the object with the given 
#     integer iterator iterator.

# int next() Returns the next element in the array and moves the pointer to the next element.
# boolean hasNext() Returns true if there are still elements in the array.
# int peek() Returns the next element in the array without moving the pointer.
# Note: Each language may have a different implementation of the constructor and
# Iterator, but they all support the int next() and boolean hasNext() functions.

 

# Example 1:

# Input
# ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
# [[[1, 2, 3]], [], [], [], [], []]
# Output
# [null, 1, 2, 2, 3, false]

# Explanation
# PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
# peekingIterator.next();    // return 1, the pointer moves to the next element [1,2,3].
# peekingIterator.peek();    // return 2, the pointer does not move [1,2,3].
# peekingIterator.next();    // return 2, the pointer moves to the next element [1,2,3]
# peekingIterator.next();    // return 3, the pointer moves to the next element [1,2,3]
# peekingIterator.hasNext(); // return False



# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """


class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.index = 0

    def hasNext(self):
        return self.index < len(self.nums)

    def next(self):
        if self.hasNext():
            val = self.nums[self.index]
            self.index += 1
            return val
        else:
            return None
        
class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None

    def peek(self):
        return self.next_element

    def next(self):
        result = self.next_element
        self.next_element = self.iterator.next() if self.iterator.hasNext() else None
        return result

    def hasNext(self):
        return self.next_element is not None

# Input
commands = ["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
values = [[[1, 2, 3]], [], [], [], [], []]

# Output
output = []
peekingIterator = None

for command, value in zip(commands, values):
    if command == "PeekingIterator":
        peekingIterator = PeekingIterator(Iterator(value[0]))
        output.append(None)
    elif command == "next":
        output.append(peekingIterator.next())
    elif command == "peek":
        output.append(peekingIterator.peek())
    elif command == "hasNext":
        output.append(peekingIterator.hasNext())

print(output)
