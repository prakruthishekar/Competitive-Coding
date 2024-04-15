# Minimum Meeting Rooms (hard) #
# Given a list of intervals representing the start and end time of ‘N’ meetings, find the minimum number of rooms required to hold all the meetings.

# Example 1:

# Meetings: [[1,4], [2,5], [7,9]]
# Output: 2
# Explanation: Since [1,4] and [2,5] overlap, we need two rooms to hold these two meetings. [7,9] can 
# occur in any of the two rooms later.
# Example 2:

# Meetings: [[6,7], [2,4], [8,12]]
# Output: 1
# Explanation: None of the meetings overlap, therefore we only need one room to hold all meetings.
# Example 3:

# Meetings: [[1,4], [2,3], [3,6]]
# Output:2
# Explanation: Since [1,4] overlaps with the other two meetings [2,3] and [3,6], we need two rooms to 
# hold all the meetings.
 
# Example 4:

# Meetings: [[4,5], [2,3], [2,4], [3,5]]
# Output: 2
# Explanation: We will need one room for [2,3] and [3,5], and another room for [2,4] and [4,5].
 
# Here is a visual representation of Example 4:

from heapq import *

def min_meeting_rooms(meetings):
    meetings.sort(key=lambda x: x[0])
    minHeap = []
    minRooms = 0
    for meeting in meetings:
        # Remove all the meetings that have ended
        while len(minHeap) > 0 and meeting[0] >= minHeap[0][0]:
            heappop(minHeap)

        # Push the end time along with the meeting
        heappush(minHeap, (meeting[1], meeting))

        minRooms = max(minRooms, len(minHeap))
        
    return minRooms
print(min_meeting_rooms([[1,4], [2,5], [7,9]]))
print(min_meeting_rooms([[6,7], [2,4], [8,12]]))
print(min_meeting_rooms([[1,4], [2,3], [3,6]]))
print(min_meeting_rooms([[4,5], [2,3], [2,4], [3,5]]))



# So our algorithm will look like this:

# Sort all the meetings on their start time.
# Create a min-heap to store all the active meetings. This min-heap will also be used to find the active meeting with the smallest end time.
# Iterate through all the meetings one by one to add them in the min-heap. Let’s say we are trying to schedule the meeting m1.
# Since the min-heap contains all the active meetings, so before scheduling m1 we can remove all meetings from the heap that have ended before m1, i.e., remove all meetings from the heap that have an end time smaller than or equal to the start time of m1.
# Now add m1 to the heap.
# The heap will always have all the overlapping meetings, so we will need rooms for all of them. Keep a counter to remember the maximum size of the heap at any time which will be the minimum number of rooms needed.



# Time complexity #
# The time complexity of the above algorithm is O(N∗logN), where ‘N’ is the total number of meetings. This is due to the sorting that we did in the beginning. Also, while iterating the meetings we might need to poll/offer meeting to the priority queue. Each of these operations can take 
#                                                 O(logN). Overall our algorithm will take O(NlogN).

# Space complexity #
# The space complexity of the above algorithm will be O(N) which is required for sorting. Also, in the worst case scenario, we’ll have to insert all the meetings into the Min Heap (when all meetings overlap) which will also take 
# O(N) space. The overall space complexity of our algorithm is O(N).