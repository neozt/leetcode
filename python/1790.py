class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        have_swapped = False
        diff_index = None

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if have_swapped:
                    return False

                if diff_index is None:
                    diff_index = i
                else:
                    # Try swap i and diff_index
                    if s1[diff_index] == s2[i] and s1[i] == s2[diff_index]:
                        diff_index = None
                        have_swapped = True
                    else:
                        return False

        return diff_index is None

print(Solution().areAlmostEqual('bank', 'kanb'))
print(Solution().areAlmostEqual('attack', 'defend'))
print(Solution().areAlmostEqual('kelb', 'kelb'))
