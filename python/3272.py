class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def find_all_palindromes(n_max):
            palindromes_ = []
            def build_palindrome(i: int, d: list[str]) -> None:
                if i >= ((n_max + 1) // 2):
                    _palindrome = ['0'] * n_max
                    for _idx in range(((n_max + 1) // 2)):
                        _palindrome[_idx] = _palindrome[n_max - 1 - _idx] = d[_idx]

                    nonlocal palindromes_
                    palindromes_.append(''.join(_palindrome))
                    return

                start = 0
                if i == 0:
                    start = 1
                for j in range(start, 10):
                    d.append(str(j))
                    build_palindrome(i + 1, d)
                    d.pop()

            build_palindrome(0, [])

            return palindromes_

        result = 0
        palindromes = find_all_palindromes(n)
        palindrome_set = set()
        for palindrome in palindromes:
            if int(palindrome) % k == 0:
                palindrome_set.add(''.join(sorted(palindrome)))

        for i in range(10 ** (n - 1), 10 ** n):
            if ''.join(sorted(str(i))) in palindrome_set:
                result += 1

        return result

print(Solution().countGoodIntegers(3, 5))
print(Solution().countGoodIntegers(1, 4))
print(Solution().countGoodIntegers(5, 6))
