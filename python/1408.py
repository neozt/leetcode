from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len, reverse=True)
        result = []
        for i in range(len(words)):
            current = words[i]
            for j in range(i):
                if words[j].count(current) >= 1:
                    result.append(current)
                    break

        return result


print(Solution().stringMatching(["mass", "as", "hero", "superhero"]))
print(Solution().stringMatching(["leetcode","et","code"]))
print(Solution().stringMatching(["blue","green","bu"]))
print(Solution().stringMatching(["leetcoder","leetcode","od","hamlet","am"]))


