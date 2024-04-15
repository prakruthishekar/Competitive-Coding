
def productExceptSelf(nums):
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

arr  = [1,2,3,4]
print(productExceptSelf(arr))  