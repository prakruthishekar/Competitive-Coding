# You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

# Return the minimum area of a rectangle formed from these points, with 
# sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

 

# Example 1:


# Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# Example 2:


# Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2

def minAreaRect(points) -> int:
        visited = set()
        min_area = float('inf')

        for x1, y1 in points:
            for x2, y2 in visited:
                if (x1, y2) in visited and (x2, y1) in visited:
                    area = abs(x1 - x2) * abs(y1 - y2)
                    min_area = min(min_area, area)
            visited.add((x1,y1))
        
        return 0 if min_area == float('inf') else min_area

print(minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))


# https://leetcode.com/problems/minimum-area-rectangle/