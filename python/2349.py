import heapq
from collections import defaultdict


class NumberContainers:

    def __init__(self):
        self.numbers = {}
        self.number_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        heapq.heappush(self.number_to_indices[number], index)
        self.numbers[index] = number

    def find(self, number: int) -> int:
        indices = self.number_to_indices[number]
        while indices and self.numbers[indices[0]] != number:
            heapq.heappop(indices)

        if not indices:
            return -1

        return indices[0]

obj = NumberContainers()
print(obj.find(10))
obj.change(2, 10)
obj.change(1, 10)
obj.change(3, 10)
obj.change(5, 10)
print(obj.find(10))
obj.change(1, 20)
print(obj.find(10))