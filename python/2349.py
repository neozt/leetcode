import bisect
from collections import defaultdict


class NumberContainers:

    def __init__(self):
        self.numbers = {}
        self.number_to_indices = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if index in self.numbers:
            previous_number = self.numbers[index]
            remove_index = bisect.bisect_left(self.number_to_indices[previous_number], index)
            self.number_to_indices[previous_number].pop(remove_index)

        bisect.insort_right(self.number_to_indices[number], index)
        self.numbers[index] = number

    def find(self, number: int) -> int:
        return self.number_to_indices[number][0] if self.number_to_indices[number] else -1


obj = NumberContainers()
print(obj.find(10))
obj.change(2, 10)
obj.change(1, 10)
obj.change(3, 10)
obj.change(5, 10)
print(obj.find(10))
obj.change(1, 20)
print(obj.find(10))