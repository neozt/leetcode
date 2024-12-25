from collections import defaultdict
from typing import List


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(formula: str) -> List[str | int]:
            result = []
            i = 0
            while i < len(formula):
                if formula[i] == '(' or formula[i] == ')':
                    result.append(formula[i])
                    i += 1
                elif formula[i] in '0123456789':
                    n = formula[i]
                    i += 1
                    while i < len(formula) and formula[i] in '0123456789':
                        n += formula[i]
                        i += 1
                    result.append(int(n))

                else:
                    element = formula[i]
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        element += formula[i]
                        i += 1
                    result.append(element)

            return result

        def pad(tokens: List[str | int]) -> List[str | int]:
            result = []
            for i, token in enumerate(tokens):
                result.append(token)
                if not isinstance(token, int) and token != '(' and (i + 1 >= len(tokens) or not isinstance(tokens[i + 1], int)):
                    result.append(1)

            return result


        #print(parse(formula))
        #print(pad(parse(formula)))

        parsed_tokens = pad(parse(formula))
        stack = [defaultdict(int)]
        i = 0
        while i < len(parsed_tokens):
            token = parsed_tokens[i]
            if token == '(':
                stack.append(defaultdict(int))
                i += 1
            elif token == ')':
                multiplier = parsed_tokens[i + 1]
                previous = stack.pop()
                top = stack[-1]
                for el, count in previous.items():
                    top[el] += count * multiplier
                i += 2
            else:
                count = parsed_tokens[i + 1]
                stack[-1][parsed_tokens[i]] += count
                i += 2

        return ''.join(map(lambda x: x[0] + (str(x[1]) if x[1] != 1 else ''), sorted(stack[0].items())))

print(Solution().countOfAtoms("H2O"))
print(Solution().countOfAtoms("Mg(OH)2"))
print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
