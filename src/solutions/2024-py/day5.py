# =============================================================================
# Ruth Wertz
# AOC 2024 - Day 5
# https://github.com/HumbleUnicorn/Advent-of-Code/tree/main/src/solutions/2024-py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# (1) parse instructions to dict {pg:[pgs that come after]} and updates <list>
# (2) read L to R: if R pg in dict[L], order is OK 
# (3) sum middle val as += int(line[int(n/2)])
#
# // PART 2 //
# (1) read only "bad" lines
# (2) read L to R: if R pg in dict[L], pass (all passed, append to end)
#                  else insert "R" at "L" index location
# (3) sum middle val as += int(line[int(n/2)])
#        
# =============================================================================

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

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
        return(data)

def parseInst(data, type=0): #return 0: master <list>, 1: rules <dict>, 2: updates <list> 
    o = []; u = []; d = {}
    for line in data:
        if "|" in line:
            o.append(line.split("|"))
        elif len(line) >5:
            u.append(line.split(","))
    for line in o:
        if line[0] not in d:
            d.update({line[0]:[]})
        d[line[0]].append(line[1])
    keys = list(d.keys()); vals = list(d.values())
    p = keys
    for val in vals:
        p += val
    p = list(set(p))    
    if type == 1:
        return(d)
    elif type == 2:
        return(u)
    else:
        return(p)

def getPageSum_pt1(data, ruleDict): #return <int> 
    sum=0
    for line in data:
        n = len(line)
        m = int(line[int(n/2)])
        for i in range(n-1,0,-1):
            pg = line[i]; pp = line[i-1]
            try:
                pp = ruleDict[pp]
            except:
                pp = []
            if pg in pp:
                pass
            else:
                m=0
        sum += m
    return(sum)

def getBadPages_pt2(data, ruleDict): #return <list> 
    b = []
    for line in data:
        n = len(line)
        bad = False
        for i in range(n-1,0,-1):
            pg = line[i]; pp = line[i-1]
            try:
                pp = ruleDict[pp]
            except:
                pp = []
            if pg in pp:
                pass
            else:
                bad = True
        if bad:
           b.append(line)
    return(b)

def getPageSum_pt2(data, ruleDict): #return <int> 
    sum = 0
    for line in data:
        n = len(line); sorted = []
        for i in range(n):
            pg = line[i]
            if pg not in ruleDict:
                ruleDict.update({pg:[]})
            if len(sorted) == 0:
                sorted.append(pg)
            else:
                for item in sorted:
                    if pg not in ruleDict[item]:
                        sorted.insert(sorted.index(item),pg)
                        break
                    else:
                        pass
                if pg not in sorted:
                    sorted.append(pg)
        sum += int(sorted[int(n/2)])
    return(sum)

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

input = readSrc('day5_test',False)
rules = parseInst(input,1); #print(rules)
updates = parseInst(input,2); #print(updates)
bad = getBadPages_pt2(updates,rules); #print(bad)

pgSum_ok = getPageSum_pt1(updates,rules)
print(f"Test Output1: {pgSum_ok}")

pgSum_mod = getPageSum_pt2(bad,rules)
print(f"Test Output2: {pgSum_mod}")
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

input = readSrc('day5',False)
rules = parseInst(input,1); #print(rules)
updates = parseInst(input,2); #print(updates)
bad = getBadPages_pt2(updates,rules); #print(bad)

pgSum_ok = getPageSum_pt1(updates,rules)
print(f"Output1: {pgSum_ok}")

pgSum_mod = getPageSum_pt2(bad,rules)
print(f"Output2: {pgSum_mod}")