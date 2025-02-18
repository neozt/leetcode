class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = set()
        def helper(current_str: str, current_index: int) -> str | None:
            if current_index == len(pattern) + 1:
                return current_str

            for i in range(1, 10):
                # Guards
                if i in used:
                    continue

                if current_index > 0:
                    if pattern[current_index - 1] == 'I' and i <= int(current_str[-1]):
                        continue
                    if pattern[current_index - 1] == 'D' and i >= int(current_str[-1]):
                        continue

                used.add(i)
                candidate = helper(current_str + str(i), current_index + 1)
                if candidate is not None:
                    return candidate
                used.remove(i)

            return None

        return helper('', 0)

print(Solution().smallestNumber('IIIDIDDD'))
print(Solution().smallestNumber('DDD'))
