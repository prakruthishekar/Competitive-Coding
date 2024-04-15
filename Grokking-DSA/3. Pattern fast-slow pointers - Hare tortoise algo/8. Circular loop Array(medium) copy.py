# Cycle in a Circular Array (hard) #
# We are given an array containing positive and negative numbers. 
# Suppose the array contains a number ‘M’ at a particular index. Now, 
# if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is 
# negative move backwards ‘M’ indices. You should assume that the array 
# is circular which means two things:

# If, while moving forward, we reach the end of the array, we will jump 
# to the first element to continue the movement.
# If, while moving backward, we reach the beginning of the array, we will
#  jump to the last element to continue the movement.
# Write a method to determine if the array has a cycle. The cycle should have more than one element and should follow one direction which means the cycle should not contain both forward and backward movements.

# Example 1:

# Input: [1, 2, -1, 2, 2]
# Output: true
# Explanation: The array has a cycle among indices: 0 -> 1 -> 3 -> 0
# Example 2:

# Input: [2, 2, -1, 2]
# Output: true
# Explanation: The array has a cycle among indices: 1 -> 3 -> 1
# Example 3:

# Input: [2, 1, -1, -2]
# Output: false
# Explanation: The array does not have any cycle.


def circularArrayLoop(nums) -> bool:

        def getNextIndex(nums, currentIndex):
            n = len(nums)
            nextIndex = (currentIndex + nums[currentIndex]) % n
            
            # Handle negative indices
            if nextIndex < 0:
                nextIndex += n
            
            # If the movement direction changes, return the current index
            if nums[currentIndex] * nums[nextIndex] < 0:
                return currentIndex
            
            return nextIndex

        n = len(nums)
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            slow = i
            fast = i
            
            # Move slow and fast pointers
            while True:
                # Move slow pointer
                slow = getNextIndex(nums, slow)
                
                # Move fast pointer
                fast = getNextIndex(nums, fast)
                fast = getNextIndex(nums, fast)
                
                if slow == fast:
                    break
            
            # Check if cycle length is greater than 1 and all elements have the same sign
            if slow != getNextIndex(nums, slow):
                return True
            
            # Mark the cycle as visited by setting all its elements to 0
            slow = i
            while nums[slow] != 0:
                nextIndex = getNextIndex(nums, slow)
                nums[slow] = 0
                slow = nextIndex
        
        return False


print(circularArrayLoop([1, 2, -1, 2, 2]))
print(circularArrayLoop([2, 2, -1, 2]))
print(circularArrayLoop([1,2,3,4,1]))

