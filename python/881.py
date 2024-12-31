from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        num_boats = 0

        i = 0
        j = len(people) - 1

        while (i <= j):
            if people[i] + people[j] <= limit:
                # Slim person is accounted for
                i += 1
            j -= 1 # Heavy person is accounted for
            num_boats += 1 # Contains 1 heavy person and optionally 1 slim person if he fits

        return num_boats

print(Solution().numRescueBoats([1, 2], 3))
print(Solution().numRescueBoats([3,2,2,1], 3))
print(Solution().numRescueBoats([3,5,3,4], 5))
