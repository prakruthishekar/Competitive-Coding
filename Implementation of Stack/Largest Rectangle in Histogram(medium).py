# Given an array of integers heights representing the histogram's bar
# height where the width of each bar is 1, return the area of the largest 
# rectangle in the histogram.

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# # The largest rectangle is shown in the red area, which has an area = 10 units.


# Input: heights = [2,4]
# Output: 4


def largestRectangleArea(heights):
    heights.append(0)
    stack = [-1]
    ans = 0
    for i in range(len(heights)):
        while heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            ans = max(ans, height * width)
        stack.append(i)
    heights.pop()
    return ans

print(largestRectangleArea([2,1,5,6,2,3]))