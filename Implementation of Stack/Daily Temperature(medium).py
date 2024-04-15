# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to 
# wait after the ith day to get a warmer temperature. If there is no future day
# for which this is possible, keep answer[i] == 0 instead.

 

# Example 1:

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:

# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]

def dailyTemperatures(nums):
        res = [0] * len(nums)
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]: #find the higher
                cur = stack.pop()
                res[cur] = i - cur
            stack.append(i)                    
        return res


print(dailyTemperatures([73,74,75,71,69,72,76,73]))