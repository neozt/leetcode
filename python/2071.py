import heapq
from typing import List

# TODO: incorrect solution
class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        task_heap = []
        adjusted_task_heap = []
        worker_heap = workers.copy()
        heapq.heapify(worker_heap)
        pills_remaining = pills

        for i, task in enumerate(tasks):
            heapq.heappush(task_heap, (task, i))
            heapq.heappush(adjusted_task_heap, (task - strength, i))


        result = 0

        used = [False] * len(tasks)

        while worker_heap:
            worker = heapq.heappop(worker_heap)

            while used[task_heap[0][1]]:
                heapq.heappop(task_heap)

            while used[adjusted_task_heap[0][1]]:
                heapq.heappop(adjusted_task_heap)

            if task_heap and worker >= task_heap[0][0]:
                _, i = heapq.heappop(task_heap)
                result += 1
                used[i] = True
            elif pills_remaining > 0 and adjusted_task_heap and worker >= adjusted_task_heap[0][0]:
                _, i = heapq.heappop(adjusted_task_heap)
                result += 1
                pills_remaining -= 1
                used[i] = True

        return result


print(Solution().maxTaskAssign([3,2,1], [0,3,3], 1, 1))
print(Solution().maxTaskAssign([5,4], [0,0,0], 1, 5))
print(Solution().maxTaskAssign([10, 15,30], [0,10,10,10,10], 3, 10))




