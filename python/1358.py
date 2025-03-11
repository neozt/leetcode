from collections import deque


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a_indices = deque([])
        b_indices = deque([])
        c_indices = deque([])
        indices_map = {
            'a': a_indices,
            'b': b_indices,
            'c': c_indices
        }

        for i, ch in enumerate(s):
            arr = indices_map[ch]
            if arr is not None:
                arr.append(i)

        result = 0

        for i in range(len(s)):
            if a_indices and a_indices[0] < i:
                a_indices.popleft()
            if b_indices and b_indices[0] < i:
                b_indices.popleft()
            if c_indices and c_indices[0] < i:
                c_indices.popleft()

            if not a_indices or not b_indices or not c_indices:
                break

            r = max(a_indices[0], b_indices[0], c_indices[0])
            result += len(s) - r

        return result

print(Solution().numberOfSubstrings('abcabc')) # 10
print(Solution().numberOfSubstrings('aaacb')) # 3
print(Solution().numberOfSubstrings('abc')) # 1