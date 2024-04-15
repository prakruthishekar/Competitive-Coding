# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum
# minutes difference between any two time-points in the list.
 

# Example 1:

# Input: timePoints = ["23:59","00:00"]
# Output: 1
# Example 2:

# Input: timePoints = ["00:00","23:59","00:00"]
# Output: 0


def findMinDifference(timePoints) -> int:
        for i, time in enumerate(timePoints):
            hours, minutes = time.split(":")
            min_past_midnight = int(hours) * 60 + int(minutes)
            timePoints[i] = min_past_midnight
        
        timePoints.sort()
        res = 1440 + timePoints[0] - timePoints[-1] # edge case if we have "23:59" and "00:00"
        for i in range(1, len(timePoints)):
            res = min(res, timePoints[i] - timePoints[i-1])

        return res

print(findMinDifference(timePoints = ["23:59","00:00"]))
print(findMinDifference(timePoints = ["00:00","23:59","00:00"]))
