from solver import Solver


#################### Part 1 ####################
with open("everybody_codes_e2024_q01_p1.txt", 'r') as f:
    part1 = f.readline()
solver = Solver()
result = solver.Solve1(part1)
print(f"Answer of part 1: {result}")


#################### Part 2 ####################
with open("everybody_codes_e2024_q01_p2.txt", 'r') as f:
    part2 = f.readline()
result = solver.Solve2(part2)
print(f"Answer of part 2: {result}")


#################### Part 3 ####################
with open("everybody_codes_e2024_q01_p3.txt", 'r') as f:
    part3 = f.readline()
result = solver.Solve3(part3)
print(f"Answer of part 3: {result}")
