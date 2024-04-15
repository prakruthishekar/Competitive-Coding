# There are several cards arranged in a row, and each card has an associated number of points. 
# The points are given in the integer array cardPoints.

# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

# Your score is the sum of the points of the cards you have taken.

# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

# Example 1:

# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, 
# choosing the rightmost card first will maximize your total score. 
# The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
# Example 2:

# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always be 4.
# Example 3:

# Input: cardPoints = [9,7,7,9,7,7,9], k = 7
# Output: 55
# Explanation: You have to take all the cards. Your score is the sum of points of all cards.

def maxPoints(cardPoints , k):

    total_points = sum(cardPoints)

    if len(cardPoints) == k:
        return total_points
    window_size = len(cardPoints) - k
    min_subarray_sum = float('inf')
    current_sum = 0
    iterator = 0
    for i in range(len(cardPoints)):
        current_sum += cardPoints[i]
        if i >= window_size - 1:
            min_subarray_sum = min(min_subarray_sum, current_sum)
            current_sum -= cardPoints[iterator]
            iterator += 1
    return total_points - min_subarray_sum

# print(maxPoints(cardPoints = [2,2,2], k = 2))
# print(maxPoints([2,2,2], k = 2))
print(maxPoints(cardPoints = [9,7,7,9,7,7,9], k = 7))

