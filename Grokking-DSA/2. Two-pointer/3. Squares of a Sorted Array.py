
# def squaresOfSortedArray(arr):
#     highestScore = len(arr) - 1
#     left = 0
#     right = len(arr) - 1
#     response = [0] * len(arr)
#     # response = [0 for _ in range(len(arr))]         ->   Initialize array with zero values  
#     while(left <= right):
#         leftSquare = (arr[left] ** 2)
#         rightSquare = (arr[right] ** 2)
#         if(leftSquare >= rightSquare):
#             response[highestScore] = leftSquare
#             highestScore -= 1
#             left +=1
#         else:
#             response[highestScore] = rightSquare
#             highestScore -= 1
#             right -= 1    
#     return response

# arr = [-4,-3,0,5,9]
# sortedArray = squaresOfSortedArray(arr)
# print("The squares of each number sorted in non-decreasing order would be : ", sortedArray)




def sortedSquares(nums):
    squares = [0] * len(nums)
    l = 0
    r = len(nums) - 1
    for i in range(len(nums)-1, -1, -1):
        if abs(nums[r]) > abs(nums[l]):
            squares[i] = nums[r] ** 2
            r -= 1
        else:
            squares[i] = nums[l] ** 2
            l += 1
    return squares

nums = [-4,-3,0,5,9]
sortedrArray = sortedSquares(nums)
print(sortedrArray)   
