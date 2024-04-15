def findKthPositive(nums, k: int) -> int:
    lo = 0
    hi = len(nums) - 1
    while(lo <= hi):
        mid = lo + (hi - lo) // 2
        missing = nums[mid] - (mid + 1)  
# ideally, arr[i] should hold i + 1 value i.e arr[0] = 1, arr[1] = 2..etc
        if missing >= k:
            hi = mid - 1
        else:
            lo = mid + 1
    return hi + k + 1


# Compare the number of missing integers missing with the target value k:
# If missing is greater than or equal to k, it means that the k-th missing 
# positive number is located before or at the middle index. Therefore, 
# update hi to mid - 1 to search in the left subarray.

# If missing is less than k, it means that the k-th missing positive number 
# is located after the middle index. Therefore, update lo to mid + 1 to 
# search in the right subarray.

# Repeat steps 3-5 until lo becomes greater than hi, indicating that the
# search space has been exhausted.
# Once the while loop terminates, return the result hi + k + 1. Adding 
# k accounts for the missing numbers before the last checked middle index, 
# and adding 1 adjusts for the fact that array indices are zero-based.


print(findKthPositive([2,3,4,7,11], 5))