# Problem Statement #
# Given a list of non-overlapping intervals sorted by their start time, 
# insert a given interval at the correct position and merge all necessary 
# intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
# Output: [[1,3], [4,7], [8,12]]
# Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].
# Example 2:

# Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
# Output: [[1,3], [4,12]]
# Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12],
#  we merged them into [4,12].

# Example 3:

# Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
# Output: [[1,4], [5,7]]
# Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].


def insert_interval(intervals, newInterval):
    # Constant to help us access start point and end point of interval
        START, END = 0, 1
        s, e = newInterval[START], newInterval[END]      
        left, right = [], [] 

        for cur_interval in intervals:
            
            if cur_interval[END] < s:
                # current interval is on the left-hand side of newInterval
                left += [ cur_interval ]
                
            elif cur_interval[START] > e:
                # current interval is on the right-hand side of newInterval
                right += [ cur_interval ]
                
            else:
                # current interval has overlap with newInterval
                # merge and update boundary
                s = min(s, cur_interval[START])
                e = max(e, cur_interval[END])
                
        return left + [ [s, e] ] + right 

print(insert_interval([[1,3],[6,9]], [2,5]))  
print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  