from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        decreasing = [0]
        result = 0
        previous_min = 0
        for i in range(1, n + 1):
            if i == n or ratings[i] >= ratings[decreasing[-1]]:
                previous_rating = float('-inf')
                previous_candy = 0
                for j in range(len(decreasing) - 1, -1, -1):
                    rating = ratings[decreasing[j]]
                    if rating > previous_rating:
                        candy = previous_candy + 1
                    else:
                        candy = previous_candy

                    if j == 0 and decreasing[j] != 0 and ratings[decreasing[j]] > ratings[decreasing[j] - 1]:
                        candy = max(previous_min + 1, candy)
                    result += candy
                    previous_candy = candy
                    previous_rating = rating
                    if j == len(decreasing) - 1:
                        current_min = candy

                previous_min = current_min
                decreasing = [i]
            else:
                decreasing.append(i)

        return result


print(Solution().candy([1,0,2]))
print(Solution().candy([1,2,2]))
print(Solution().candy([1,3,2,2,1]))
print(Solution().candy([1,2,87,87,87,2,1]))
print(Solution().candy([1,3,4,5,2]))
