class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        while l < r:
            mid = ((l + r )//2)
            # print(int(mid))
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                l = mid + 1
            
            elif nums[mid] > target:
                r = mid     
        return -1

a =  Solution()
print(a.search([-1,0,3,5,9,12],3) )      


