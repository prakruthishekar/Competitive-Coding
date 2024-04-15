def find_second_largest(nums):
    if len(nums) < 2:
        return None

    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest

nums = [5, 2, 8, 9, 1]
second_largest = find_second_largest(nums)
print("Second largest number:", second_largest)