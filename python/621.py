from collections import Counter
from itertools import count
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = Counter(tasks)
        print(task_count)

        max_count = max(task_count.values())
        values_with_max_count = len([1 for count in task_count.values() if count == max_count])
        bottleneck = (max_count - 1) * (n + 1) + values_with_max_count
        return max(bottleneck, len(tasks))



print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(["A","C","A","B","D","B"], 1))
print(Solution().leastInterval(["A","A","A", "B","B","B"], 3))
