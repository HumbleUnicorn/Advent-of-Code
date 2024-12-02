# =============================================================================
# Ruth Wertz
# AOC 2024 - Day 1
# https://github.com/HumbleUnicorn/Advent-of-Code/tree/main/src/solutions/2024-py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# (1) parse line into left, right lists
# (2) sort ascending   
# (3) for l, r in left, right: append diff = abs(r-l) 
# (4) sum(diff)
#
# // PART 2 //
# (1) for l in left, n = count of "l" in right
# (2) append sim_score = l*n
# (3) sum(sim)
#        
# =============================================================================

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

# from collections import Counter
# imprt re

def readSrc (fname):
    with open(f'ignore/{fname}.txt', 'r') as file:
        data = []
        for line in file:
            line = line.strip()
            line = line.split('   ')
            data.append(line)
        return(data) # ===> <list>

def parseData(data):
    left = []; right = []
    for line in data:
        left.append(int(line[0]))
        right.append(int(line[1]))
    left.sort(); right.sort()
    return(left,right)

def getDistance (left,right):
    diff = []
    for l, r in zip(left,right):
        diff.append(abs(r-l))
    return(diff)

def getSimilarity (left,right):
    sim = []
    for l in left:
        n = right.count(l)
        sim.append(l*n)
    return(sim)


# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

test1 = readSrc('day1_test'); #print(test1)
right = parseData(test1)[0]; left = parseData(test1)[1]

diff = getDistance(right,left)
test_output1 = sum(diff); #print(diff)
print(f"Test Output1: {test_output1}")

sim = getSimilarity(right,left)
test_output2 = sum(sim); #print(sim)
print(f"Test Output2: {test_output2}")
   
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

day1 = readSrc('day1'); #print(day1)
right = parseData(day1)[0]; left = parseData(day1)[1]

diff = getDistance(right,left)
output1 = sum(diff); #print(diff)
print(f"Output1: {output1}")

sim = getSimilarity(right,left)
output2 = sum(sim); #print(sim)
print(f"Output2: {output2}")