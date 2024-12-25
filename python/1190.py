class Solution:
    def reverseParentheses(self, s: str) -> str:
        stackOfStacks = [[]]
        for ch in s:
            if ch == '(':
                stackOfStacks.append([])
            elif ch == ')':
                currentStack = stackOfStacks.pop()
                previousStack = stackOfStacks[-1]
                while currentStack:
                    previousStack.append(currentStack.pop())
            else:
                stackOfStacks[-1].append(ch)

        return ''.join(stackOfStacks[0])


print(Solution().reverseParentheses('(abcd)'))
print(Solution().reverseParentheses("(u(love)i)"))
print(Solution().reverseParentheses("(ed(et(oc))el)"))
