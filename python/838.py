class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        LEFT = 'L'
        RIGHT = 'R'
        UPRIGHT = '.'

        n = len(dominoes)
        forces = [0] * n

        current_force = 0
        for i in range(n):
            if dominoes[i] == RIGHT:
                current_force = n
            elif dominoes[i] == LEFT:
                current_force = 0
            else:
                current_force = max(current_force - 1, 0)

            forces[i] += current_force

        current_force = 0
        for i in reversed(range(n)):
            if dominoes[i] == LEFT:
                current_force = n
            elif dominoes[i] == RIGHT:
                current_force = 0
            else:
                current_force = max(current_force - 1, 0)

            forces[i] -= current_force

        result = []
        for force in forces:
            if force == 0:
                dir = UPRIGHT
            elif force > 0:
                dir = RIGHT
            else:
                dir = LEFT

            result.append(dir)

        return ''.join(result)

print(Solution().pushDominoes('RR.L'))
print(Solution().pushDominoes('.L.R...LR..L..'))
print(Solution().pushDominoes('.L.R...LR..L..'))
print(Solution().pushDominoes('R.......L.R.........'))