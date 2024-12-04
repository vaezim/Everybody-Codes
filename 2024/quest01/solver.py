class Solver:
    def __init__(self):
        pass

    def Solve1(self, line):
        points = { 'A': 0, 'B': 1, 'C': 3 }
        sum = 0
        for c in line:
            sum += points[c]
        return sum

    def Solve2(self, line):
        sum = 0
        points = { 'A': 0, 'B': 1, 'C': 3, 'D': 5 }
        for i in range(0, len(line), 2):
            a, b = line[i], line[i+1]
            if a != 'x' and b != 'x':
                sum += points[a] + points[b] + 2
            elif a != 'x':
                sum += points[a]
            elif b != 'x':
                sum += points[b]
        return sum

    def Solve3(self, line):
        sum = 0
        points = { 'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0 }
        for i in range(0, len(line), 3):
            a, b, c = line[i], line[i+1], line[i+2]
            sum += points[a] + points[b] + points[c]
            x_count = line[i:i+3].count('x')
            if x_count == 1:
                sum += 2
            elif x_count == 0:
                sum += 6
        return sum
