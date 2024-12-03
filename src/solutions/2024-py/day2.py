# =============================================================================
# Ruth Wertz
# AOC 2024 - Day 2
# https://github.com/HumbleUnicorn/Advent-of-Code/tree/main/src/solutions/2024-py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# (1) parse line as list of <int>
# (2) scan list; diff = list[i+1]-list[i] ===> Return <bool> 
#        Rule 1: IF all diff > 0 or all diff < 0 AND
#        Rule 2: abs(diff) <= 3 ==> return True
# (3) num_pass = 0; +=1 if scan = True
#
# // PART 2 //
# (1) modify parse to list of lists [[list],[list.pop(0)],[list.pop(1)], ...]
# (2) scan list in line ==> if any True, return True
# (3) num_pass = 0; +=1 if scan = True
#        
# =============================================================================

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

# from collections import Counter
# imprt re

def readSrc (fname,split_alt=0):
    with open(f'ignore/{fname}.txt', 'r') as file:
        data = []
        for line in file:
            line = line.strip()
            if split_alt != 0:
                line = line.split(split_alt)
            else:
                line = line.split(' ')
            data.append(line)
        return(data) # ===> <list> 

def parseReports(data, drop=0): #return: list of lists
    reports = []
    for line in data:
        for i in range(len(line)):
            line[i] = int(line[i])
        reports.append([line])
    if drop:
        for i in range(len(reports)):
            r = reports[i][0]
            new = [r]
            for j in range(len(r)):
                test = r.copy()
                test.pop(j)
                new += [test]
            reports[i] = new
    return(reports)

def scanReport(report): #return: bool
    scan = False
    for test in report:
        n = 0
        if test[1] - test[0] > 0:
            for i in range(len(test)-1):
                diff = test[i+1] - test[i]
                if diff <= 0 or abs(diff) > 3:
                    n += 1
        elif test[1] - test[0] < 0:
            for i in range(len(test)-1):
                diff = test[i+1] - test[i]
                if diff >= 0 or abs(diff) > 3:
                    n += 1
        else:
            n += 1
        if n == 0:
            scan = True
    return (scan)

def getNumSafe(reports): #return: int 
    safe = 0
    for report in reports:
        if scanReport(report):
            safe += 1
    return(safe)


# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

test2 = readSrc('day2_test'); #print(test2)
reports = parseReports(test2)
num_safe1 = getNumSafe(reports)
print(f"Test Output1: {num_safe1}")

reports = parseReports(test2,1)
num_safe2 = getNumSafe(reports)
print(f"Test Output1: {num_safe2}")
   
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

day2 = readSrc('day2')
reports = parseReports(day2)
num_safe1 = getNumSafe(reports)
print(f"Output1: {num_safe1}")

reports = parseReports(day2,1)
num_safe2 = getNumSafe(reports)
print(f"Output1: {num_safe2}")