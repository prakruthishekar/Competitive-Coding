# Design a stack-like data structure to push elements to the stack and 
# pop the most frequent element from the stack.

# Implement the FreqStack class:

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest 
# to the stack's top is removed and returned.
 

# Example 1:

# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", 
# "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]


from collections import defaultdict

class FreqStack:

    def __init__(self):
        
        # key: frequency
        # value: list of number with frequency with FIFO
        self.freq_numList_dict = defaultdict( list )
        
        # key: number
        # value: frequency
        self.num_freq_dict = defaultdict( int )
        
        # global max frequency
        self.max_frequency = 0
        

    def push(self, x: int) -> None:
        
        # update x's frequency
        self.num_freq_dict[x] += 1
        
        cur_frequency = self.num_freq_dict[x]
        
        # update globl max frequency
        self.max_frequency = max(self.max_frequency, self.num_freq_dict[x])
        
        # push x into stack with corresponding frequency level
        self.freq_numList_dict[ cur_frequency ].append( x )
        
        

    def pop(self) -> int:
        
        # pop latest element from stack with global max frequency level
        high_freq_last_element = self.freq_numList_dict[ self.max_frequency ].pop() 
        
        # update pop-out element's frequency
        self.num_freq_dict[ high_freq_last_element ] -= 1
        
        
        if not self.freq_numList_dict[ self.max_frequency ]:
            
            # update global max frequency if stack of highest level is empty
            self.max_frequency -= 1
        
        # return pop-out element
        return high_freq_last_element
            
        
# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop() 

s = FreqStack()
s.push(5)
s.push(7)
s.push(5)
s.push(7)
s.push(4)
s.push(5)
s.pop()
s.pop()
s.pop()
s.pop()


