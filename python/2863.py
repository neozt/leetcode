from typing import List


class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        xor_all = 0
        for n in derived:
            xor_all ^= n

        return xor_all == 0