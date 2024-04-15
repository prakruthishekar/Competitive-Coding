def longestConsecutive(nums) -> int:
    # for each num I will check whether num-1 exists
    # if yes, then I ignore this num
    # Otherwise if num-1 doesn't exist, then I will go till I can find num+1
    # so in a way I am only checking each number max once and once in set.
    
    st = set(nums)    
    mx = 0
    for num in nums:
        if num-1 not in st:
            tmp = 1
            while num+1 in st:
                tmp += 1
                num += 1
            mx = max(mx, tmp)
   
    return mx

print(longestConsecutive([100,4,200,1,3,2]))    