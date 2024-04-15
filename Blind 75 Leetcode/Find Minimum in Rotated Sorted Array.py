class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        
        if(len(nums) == 1):
            return nums[0]

        minValue = float('inf')
        left = 0
        right = len(nums) - 1
        while(left < right):
            if(nums[left] >= nums[right]):
                minValue = min(minValue, nums[right])
                left += 1
                right -+ 1 
            else:
                minValue = min(minValue, nums[left])
                left += 1
                right -+ 1

        return minValue        

        

    
nums = [11,13,15,17]
classObject = Solution() 
print(classObject.findMin(nums))            