class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        for ch in s:
            if ch in digits:
                stack.pop()
            else:
                stack.append(ch)

        return ''.join(stack)
