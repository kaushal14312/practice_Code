'''Geek has an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith event and intervals is sorted in ascending order by starti. He wants to add a new interval newInterval= [newStart, newEnd] where newStart and newEnd represent the start and end of this interval.

Help Geek to insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Examples:

Input: intervals = [[1,3], [4,5], [6,7], [8,10]], newInterval = [5,6]
Output: [[1,3], [4,7], [8,10]]
Explanation: The newInterval [5,6] overlaps with [4,5] and [6,7].
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,9]
Output: [[1,2], [3,10], [12,16]]
Explanation: The new interval [4,9] overlaps with [3,5],[6,7],[8,10].'''


class Solution:
    def insertInterval(self, intervals, newInterval):
        result = []
        i = 0
        n = len(intervals)

        # Step 1: Add all intervals that end before the new interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Step 2: Merge overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])  # Update start
            newInterval[1] = max(newInterval[1], intervals[i][1])  # Update end
            i += 1

        # Add the merged new interval
        result.append(newInterval)

        # Step 3: Add the remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result