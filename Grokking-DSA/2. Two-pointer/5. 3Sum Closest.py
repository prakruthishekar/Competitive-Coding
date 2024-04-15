# class Solution:
#     def threeSumClosest(self, nums, target) -> int:
#         nums.sort()
#         res = sum(nums[:3])
        
#         for i in range(len(nums)-2):
#             l=i+1
#             r=len(nums)-1
#             while l<r:
#                 summ=nums[i]+nums[l]+nums[r]
#                 if(abs(summ-target)<abs(res-target)):
#                     res=summ
#                 if summ<target:
#                     l+=1
#                 else:
#                     r-=1
#         return res


class Solution:
    def threeSumClosest(self, nums, target) -> int:
        
        nums.sort()
                
        res_small = float("-inf")
        res_great = float("inf")
        
        for i in range(len(nums) - 2):
            
            if i > 0 and nums[i] == nums[i-1]: # handling duplicates
                continue
                
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                
                summ = nums[i] + nums[left] + nums[right]
                
				# just return, in the problem of 3 sum, we need to do something here.
				# But here we only need to return
                if summ == target:
                    return target
                
                elif summ < target:
                    left += 1
                    res_small = max(res_small, summ)
                
                else:
                    right -= 1
                    res_great = min(res_great, summ)
        
        if abs(res_small - target) < abs(res_great - target):
            return res_small
        else:
            return res_great

nums = [-1,2,1,-4]
classObject = Solution()
print(classObject.threeSumClosest(nums, 1))        