

# def find_is_array_is_Circular(nums) -> bool:

#         p = 0
#         q = 0

#         while True:
#             if (p < 0 or q < 0 or p > len(nums) or q > len(nums)):
#                 return False
            
#             p = nums[p]

#             if p == q:
#                 return True

#             if (p < 0 or p > len(nums)):
#                 return False
            
#             p = nums[p]

#             if p == q:
#                 return True
            
#             q = nums[q]

#             if p == q:
#                 return True
            

def find_is_array_is_Circular(nums):
    # Initialize the slow and fast pointers
    slow = fast = 0

    # Move slow and fast pointers until they meet
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            return True
        if(slow < 0 or fast < 0 or slow >=  len(nums) or fast >= len(nums)):
        
            return False

def find_the_start_of_cycle(nums):
    # Initialize the slow and fast pointers
    slow = fast = 0

    # Move slow and fast pointers until they meet
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find the start of the cycle
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # Return the start of the cycle
    return slow


def find_cycle_length(nums):
    # Initialize the slow and fast pointers
    slow = fast = 0

    # Move slow and fast pointers until they meet
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Count the steps to find the length of the cycle
    current = nums[slow]
    cycle_length = 1
    while current != slow:
        current = nums[current]
        cycle_length += 1

    # Return the length of the cycle
    return cycle_length


print(find_is_array_is_Circular([1,2,3,4,1]))
print(find_the_start_of_cycle([1,2,3,4,1]))
print(find_cycle_length([1,2,3,4,1]))

