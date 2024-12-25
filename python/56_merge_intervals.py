from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        if not intervals:
            return intervals

        intervals = sorted(intervals, key = lambda interval: interval[0])

        accumulator_interval = intervals[0]

        for interval in intervals[1:]:
            start, end = interval
            prev_start, prev_end = accumulator_interval
            if prev_end < start:
                # No overlap, add prev_interval to result and continue with current interval as accumulator
                result.append(accumulator_interval)
                accumulator_interval = [start, end]
            else:
                # Merge the intervals
                accumulator_interval = [min(start, prev_start), max(end, prev_end)]

        result.append(accumulator_interval)

        return result


print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[1,5]]))
