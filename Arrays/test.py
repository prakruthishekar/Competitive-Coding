# def searchRange(nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         right = 0
#         left = len(nums)
#         arr = []
#         first = -1
#         last = -1
#         if(len(nums) <= 0):
#            return [-1,-1]
#         # while( right <= left):
#         #     if(nums[right] == target):
#         #         if(first == -1):
#         #            first = right
#         #     if(nums[left] == target):
#         #         if(last == -1):
#         #            last = left
#         #     left -= 1
#         #     right += 1
            
#         #     if(first != -1 and last != -1):
#         #         return [first, last]
#         # return [-1,-1]
#         for i in range(0,len(nums)):
#             if(nums[i] == target):
#                 if(first == -1):
#                    first = i
#                    continue
#                 if(first != -1):
#                    last = i  

#         if(first != -1 and last != -1):
#                 return [first, last]    

#         if(first != -1 and last == -1):
#                 return [first,first]        
#         return [-1,-1]      
            
                

# nums = [1]
# target = 1
# print(searchRange(nums, target))                



from math import ceil


def find_avg_subarrays(k,arr): #defining function
  result = []
  for i in range(len(arr)-k+1): #looping through 
    
    total = 0.0
    for j in range(i, i+k):
      total += arr[j]
    result.append(total/k)
  return result

def countOdds(low, high) -> int:
    # count = 0
    # for i in range(low+1,high):
        
    #     # print((i+1) % 2)
    #     if(((i+1) % 2) == 0):
    #         count += 1
    # return count 

    print(low%2)
    print(low//2)
    print(low/2)
    oddlow_case = ((high - low)//2) + 1
    evenlow_case = (high - low)/2
    return ceil(evenlow_case) if low%2 != 1 else oddlow_case

print(countOdds(6,7))