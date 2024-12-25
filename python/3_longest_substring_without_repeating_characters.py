class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        current_best = ""
        for ch in s:
            if ch in current_best:
                last_appearance = current_best.find(ch)
                current_best = current_best[last_appearance + 1:] + ch
            else:
                current_best = current_best + ch

            if len(current_best) > longest_len:
                longest_len = len(current_best)

        return longest_len


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))