# Problem: Write a function to return the list of all such triplets instead of the count.
# How will the time complexity change in this case?

def triplets_with_smaller_sum(nums, target) -> int:
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            l = i + 1
            r = len(nums)-1
            target_sum = target - nums[i] 
            while l < r:
                if(nums[l] + nums[r] < target_sum): # found triplet
                    # since nums[r] >= nums[l], therefore we can replace nums[r] by any number
                    # between left and right to get the sum less than the target sum
                    for j in range(r,l,-1):
                         triplets.append([nums[i], nums[l], nums[j]])
                    l += 1 
                else:
                    r-=1
        return triplets

print(triplets_with_smaller_sum([-1, 0, 2, 3], 3))
print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))