# Given an array arr of unsorted numbers and a target sum, count all triplets 
# in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three
# different indices. Write a function to return the count of such triplets.

# Example 1:

# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3],
# [-1, 0, 2]
# Example 2:

# Input: [-1, 4, 2, 1, 3], target=5 
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: 
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]



def triplets_with_smaller_sum(nums, target) -> int:
        nums.sort()
        count = 0 
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            target_sum = target - nums[i] 
            while l < r:
                if(nums[l] + nums[r] < target_sum): # found triplet
                    # since nums[r] >= nums[l], therefore we can replace nums[r] by any number
                    # between left and right to get the sum less than the target sum
                    count += r - l 
                    l += 1 
                else:
                    r-=1
        return count

print(triplets_with_smaller_sum([-1, 0, 2, 3], 3))
print(triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5))


# Time complexity 
# Sorting the array will take O(N∗logN). The searchPair() will take 
# O(N). So, overall searchTriplets() will take O(N∗logN+N^​2) 
# which is asymptotically equivalent to O(N^2).

# Space complexity #
# Ignoring the space required for the output array, the space complexity of the above algorithm will be 
# O(N) which is required for sorting if we are not using an in-place sorting algorithm.

