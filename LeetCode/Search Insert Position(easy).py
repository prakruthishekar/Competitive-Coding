def searchInsert( nums, target) :

        right = len(nums)-1
        left = 0

        while(left < right):
            if(nums[right] <= target):
                return right + 1
            if(nums[left] >= target ):
                return left
            left += 1    

            if(nums[right] <= target):
                return right
            right -= 1


print(searchInsert([1,3,5,6],5)) 
print(searchInsert([1,3,5,6],7))            

