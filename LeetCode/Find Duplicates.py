def findDuplicates(nums):
    rs = []
    for num in nums:
        num = abs(num)
        if nums[num-1] < 0:
            rs.append(num)
        else:
            nums[num-1] = -nums[num-1]
    return rs


print(findDuplicates([4,3,2,7,8,2,3,1]))    