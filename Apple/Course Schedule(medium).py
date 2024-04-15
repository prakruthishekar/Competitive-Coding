# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates 
# that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

 

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you 
# should also have finished course 1. So it is impossible.




#This is a graph problem if we picture it correctly. So technically we should return false
# if the cycle exists in the graph else we should return true.

# We can solve this by using Khans Algorithm to find Topological sorting:
#     An ordering of nodes such that for every directed edge u -> v, node u comes
#     before node v in the ordering
# In orther words: each node in the ordering must appear before all the nodes that 