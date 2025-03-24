from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        days_meeting = 0
        current_day = 1

        for meeting_start, meeting_end in meetings:
            if current_day > meeting_end:
                continue

            days_meeting += meeting_end - (max(current_day, meeting_start)) + 1
            current_day = meeting_end + 1

        return days - days_meeting

print(Solution().countDays(10, [[5,7],[1,3],[9,10]]))
print(Solution().countDays(5, [[2,4],[1,3]]))
print(Solution().countDays(6, [[1,6]]))
