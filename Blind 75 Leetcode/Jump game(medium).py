# You are given an integer array nums. You are initially positioned at the array's 
# first index, and each element in the array represents your maximum jump length 
# at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. 
# Its maximum jump length is 0, which makes it impossible to reach the last index.



# def canJump(nums) -> bool:
        # reachableIndex = 0
        # for curr in range(len(nums)):
        #     if curr + nums[curr] >= reachableIndex:
        #         reachableIndex = curr + nums[curr]
        #     if curr == reachableIndex:
        #         break
                
        # return reachableIndex >= len(nums) - 1


def canJump(nums) -> bool:
        destination = len(nums) - 1
        for i in range(destination-1, -1 , -1):
            # start from the second last position of nums 
            if i + nums[i] >= destination:
                # if from ith index, we can reach destination
                # update our destination to ith index
                destination = i
        # if destination reaches 0 meaning that we can reach end from first index
        # otherwise we can't
        return destination == 0

print(canJump([2,3,0,0,4]))