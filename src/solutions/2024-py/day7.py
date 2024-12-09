# =============================================================================
# Ruth Wertz
# AOC 2024 - Day 7
# https://github.com/HumbleUnicorn/Advent-of-Code/tree/main/src/solutions/2024-py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# (1) parse to list of results and list of values
# (2) enumerate trials (possible combinations of operators)
# (3) if trial == result, resultSum += result
#
# // PART 2 //
# (1) Update operators to include concat (a <opp> b --> int(ab))
#        
# =============================================================================

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

from functools import partial
from itertools import product
from operator import add, mul

def readSrc (fname, split_alt=0): #return <list>
    with open(f'ignore/{fname}.txt', 'r') as file:
        data = []
        for line in file:
            line = line.strip()
            if split_alt == False:
                pass
            elif split_alt != 0:
                line = line.split(split_alt)
            else:
                line = line.split(' ')
            data.append(line)
        return data

def parseCalInputs (data): #return <list>, <list> (day7)
    results = []
    vals = []
    for line in input:
        a, b = line.split(": ")
        results.append(int(a))
        vals.append(eval(b.replace(*" ,")))
    return (results, vals)

def concat(a, b): #return <int> day(7)
    return int(str(a) + str(b))

def solve(operators, result, n): #return <int> (day7)
    a, b, *rem = n
    for trial in product(operators, repeat=len(n)-1):
        x = trial[0](a, b)
        for i, n in enumerate(rem, 1):
            x = trial[i](x, n)
        if x == result:
            return result
    return 0

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

inputs = readSrc('day7_test')
results, vals = parseCalInputs(inputs)
resSum1 = sum(map(partial(solve, (add, mul)), results, vals))
print(f"Test Output1: {resSum1}")
resSum2 = sum(map(partial(solve, (add, mul, concat)), results, vals))
print(f"Test Output2: {resSum2}")
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

input = readSrc('day7')
results, vals = parseCalInputs(input)
resSum1 = sum(map(partial(solve, (add, mul)), results, vals))
print(f"Output1: {resSum1}")
resSum2 = sum(map(partial(solve, (add, mul, concat)), results, vals))
print(f"Output2: {resSum2}")