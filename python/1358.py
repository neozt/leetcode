class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        previous_index = [-1] * 3
        result = 0

        for i in range(len(s)):
            # Count the number of valid substrings that end at index i by finding the rightmost point (min(previous_index)) that have a, b and c
            # Every starting point to the left of this rightmost point will form a valid substring
            previous_index[ord(s[i]) - ord('a')] = i
            result += 1 + min(previous_index)

        return result

print(Solution().numberOfSubstrings('abcabc')) # 10
print(Solution().numberOfSubstrings('aaacb')) # 3
print(Solution().numberOfSubstrings('abc')) # 1