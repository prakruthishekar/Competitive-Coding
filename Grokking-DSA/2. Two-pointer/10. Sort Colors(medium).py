class Solution:
    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        low = 0
        if(len(nums) == 1):
            return nums[0]

        while(left <= right):
            if(nums[left] == 0):
                nums[left], nums[low] = nums[low], nums[left]
                left  += 1
                low += 1
                
            elif(nums[left] == 2):
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1 

            else:
                left += 1
                               
        return nums       

nums = [2,0,2,1,1,0]
classObject = Solution()
print(classObject.sortColors(nums))        


