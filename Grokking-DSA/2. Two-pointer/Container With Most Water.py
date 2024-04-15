class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        maxArea = float('-inf')
        while(left < right):
            if(height[left] <= height[right]):
                maxArea = max(maxArea, height[left] * abs(left - right))
                left += 1
            else:   
                maxArea = max(maxArea, height[right] *  abs(left - right))
                right -= 1

        return maxArea

height  = [8,8,6,2,5,4,8,9,10]
classObject = Solution()
print(classObject.maxArea(height))
print(classObject.maxArea([2,4]))
print(classObject.maxArea([2,1,5,6,2,3]))
