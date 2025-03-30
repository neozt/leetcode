from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i, ch in enumerate(s):
            last_index[ch] = i

        partitions = []
        i = 0
        while i < len(s):
            j = i
            end = i
            while j <= end:
                end = max(end, last_index[s[j]])
                j += 1

            partitions.append(end - i + 1)
            i = j

        return partitions


print(Solution().partitionLabels('ababcbacadefegdehijhklij'))
print(Solution().partitionLabels('eccbbbbdec'))
