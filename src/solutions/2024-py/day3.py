# =============================================================================
# Ruth Wertz
# AOC 2024 - Day 3
# https://github.com/HumbleUnicorn/Advent-of-Code/tree/main/src/solutions/2024-py
# =============================================================================

# =============================================================================
#  // SOLUTION OUTLINE //
# =============================================================================
#
# // PART 1 //
# (1) import as single str
# (2) regex pattern: 
#        mul\(: "mul(" starting literal
#        (\d{1-3}): 1st num
#        \,: "," seperator literal
#        (\d{1-3}): 2nd num
#        \): ")" ending literal
# (3) append 1st_num*2nd_num to list ==> return sum
#
# // PART 2 //
# (1) split str by "do()"
# (2) split line by "don't()" and keep line[0]
# (3) revise part1 funt to handle single str or list of str
#        
# =============================================================================

# =============================================================================
#  // DEFINE FUNCTIONS // 
# =============================================================================

import re

def readSrcAsStr (fname): #return <str>
    with open(f'ignore/{fname}.txt', 'r') as file:
        f = file.read()
        data = f.strip()
        return(data) 

def parseMulStr(data): #return [<str1>, <str2>, ...] (day3)
    parse = []
    data = data.split("do()")
    for line in data:
        if "don't()" in line:
            parse.append(line.split("don't()")[0])
        else:
            parse.append(line)
    return(parse)

def getMulSum(data,split=False): #return <int> (day3)
    tuples = []
    pattern = r"mul\((\d{1,3})\,(\d{1,3})\)"
    if not split:
        matches = re.findall(pattern, data)
        for match in matches:
            tuples.append((int(match[0])*int(match[1])))
    else:
        for line in data:
            matches = re.findall(pattern, line)
            for match in matches:
                tuples.append((int(match[0])*int(match[1])))
    return(sum(tuples))

# =============================================================================
#  // TEST OUTPUT //
# =============================================================================

test1 = readSrcAsStr('day3_test1') 
testsum1 = getMulSum(test1) 
print(f"Test Output1: {testsum1}")

test2 = readSrcAsStr('day3_test2') 
parsed_test2 = parseMulStr(test2)
testsum2 = getMulSum(parsed_test2,True)  
print(f"Test Output2: {testsum2}")
   
   
# =============================================================================
#   // PUZZLE OUTPUT //
# =============================================================================

text = readSrcAsStr('day3')
sum1 = getMulSum(text)
print(f"Output1: {sum1}")

parsed_text = parseMulStr(text)
sum2 = getMulSum(parsed_text,True)  
print(f"Output2: {sum2}")
