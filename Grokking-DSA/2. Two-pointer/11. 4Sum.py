class Solution:
    def fourSum(self, nums, target):
        
        ans = [] # the result we will return
        nums.sort()
        result = set()
        for i, num in enumerate(nums):
            newTarget = target - (num)
            if i > 0 and num == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    if nums[j] + nums[left] + nums[right] > newTarget:
                        right -= 1
                    elif nums[j] + nums[left] + nums[right] < newTarget:
                        left += 1
                    else:    
                        result.add( (num, nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

                        # while nums[left - 1] == nums[left] and left < right and nums[right + 1] == nums[right]: 
                        #     left += 1
  
        return list(result)


nums = [4, 1, 2, -1, 1, -3]

classObject = Solution()
print(classObject.fourSum(nums,1))        


