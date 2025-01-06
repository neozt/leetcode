from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        from_left = [0] * len(boxes) # keeps track of how many moves are required to move all the 1's to the left of ith index, to the ith index
        ones = 0
        for i in range(0, len(boxes)):
            prev_count = 0 if i == 0 else from_left[i - 1]
            from_left[i] = prev_count + ones
            if boxes[i] == '1':
                ones += 1

        from_right = [0] * len(boxes) # keeps track of how many moves are required to move all the 1's to the right of ith index, to the ith index
        ones = 0
        for i in reversed(range(0, len(boxes))):
            prev_count = 0 if i == len(boxes) - 1 else from_right[i + 1]
            from_right[i] = prev_count + ones
            if boxes[i] == '1':
                ones += 1

        return [from_left[i] + from_right[i] for i in range(len(boxes))]


print(Solution().minOperations("110"))
print(Solution().minOperations("001011"))
