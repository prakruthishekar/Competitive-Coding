def twoSum( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    array_freq = {}
    for i, num in enumerate(nums):
        if num in array_freq:
            return [array_freq[num], i]
        array_freq[target-num] = i

nums = [2,7,11,15]
print(twoSum(nums,9))

