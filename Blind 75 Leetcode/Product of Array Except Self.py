# class Solution(object):
#     def productExceptSelf(self, nums):
#         products = 1
#         counts = []

#         for idx, num in enumerate(nums):
#             if len(counts) > 1:
#                 break
#             if num == 0:
#                 counts.append(idx)
#             else:
#                 products *= num

#         res = [0 for i in range(len(nums))]
#         if len(counts) > 1:
#             return res
#         elif len(counts) == 1:
#             res[counts[-1]] = products
#         else:
#             for i in range(len(nums)):
#                 res[i] = products // nums[i]

#         return res





# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         res = [0] * len(nums)
#         sum = 1
#         for i in nums:
#             sum = sum * i

#         for i in range(len(nums)):
#             res[i] = (sum // nums[i])

#         return res





class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        products = [1] * n

        left = 1
        for i in range(0, n-1):
            left *= nums[i]
            products[i+1] = left
        
        right = 1
        for j in range(n-1, 0, -1):
            right *= nums[j]
            products[j-1] *= right

        return products


nums  = [1,2,3,4]
classObject = Solution() 
print(classObject.productExceptSelf(nums))    
