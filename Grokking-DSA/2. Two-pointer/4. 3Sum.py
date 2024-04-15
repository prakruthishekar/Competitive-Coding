class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                target =  nums[i] + nums[l] + nums[r]
                if target == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
        return list(result)
    

    def threeSum(self, nums):
        res=[]
        nums.sort()

        for i,n in enumerate(nums):
            if i> 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                tsum = n+nums[l]+nums[r]
                if tsum >0:
                    r= r-1
                elif tsum < 0 :
                    l = l+1
                else:
                    res.append([n,nums[l],nums[r]])
                    l=l+1
                    while l<r and nums[l]==nums[l-1]:
                        l=l+1
        return res

nums =[-3, 0, 1, 2, -1, 1, -2]
classObject = Solution()
print(classObject.threeSum(nums))        