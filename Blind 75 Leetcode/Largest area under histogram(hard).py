# Given an array of integers heights representing the histogram's bar height 
# where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Input: heights = [2,4]
# Output: 4


def largestRectangleArea(heights) -> int:
        
        # store x coordination, init as -1
        stack = [ -1 ]
        
        # add zero as dummy tail 
        heights.append( 0 )
        
        # top index for stack
        top = -1
        
        # area of rectangle
        rectangle = 0
        
        # scan each x coordination and y coordination
        for x_coord, y_coord in enumerate(heights):
            
            while heights[ stack[top] ] > y_coord:
            # current height is lower than previous
            # update rectangle area from previous heights
                
                # get height
                h = heights[ stack.pop() ]
                
                # compute width
                w = x_coord - stack[top] -1 
                
                # update maximal area
                rectangle = max(rectangle, h * w)
                
            # push current x coordination into stack
            stack.append( x_coord )
            
        
        return rectangle

print(largestRectangleArea([2,1,5,6,2,3])) 
print(largestRectangleArea([2,4]))        
