# Ruth Wertz
# AOC 2023 - Day 1
# https://github.com/HumbleUnicorn/Advent-of-Code/blob/main/src/solutions/2023-py/aoc01.py


# //INPUT DATA//

day1=[]
with open('inputs/d01.txt') as f: 
    for lines in f:
        day1.append(lines) 

test1a=['1abc2','pqr3stu8vwx','a1b2c3d4e5f','treb7uchet']
test1b=['two1nine','eightwothree','abcone2threexyz','xtwone3four','4nineeightseven2','zoneight234','7pqrstsixteen']        
 
dgts = ['1','2','3','4','5','6','7','8','9']
nums = ['one','two','three','four','five','six','seven','eight','nine']
alln = dgts + nums
         
# // DEFINE FUNCTIONS // 

def firstDigit(line,nList):
  a = len(line)
  for n in nList:
    if n in line: 
      pos = line.find(n)
      if pos <= a: 
        a = pos
        val = n
      if val in nums:
        x = str(1 + nums.index(val))
      else:
        x = val
  return(x)

def lastDigit(line,nList):
  b = 0
  for n in nList:
    if n in line:
      pos = line.rfind(n)
      if pos >= b: 
        b = pos
        val = n
      if val in nums:
        y = str(1 + nums.index(val))
      else:
        y = val
  return(y)

def calVals(data,nList):
    vals = []
    for line in data:
        digit = str(firstDigit(line,nList))+(lastDigit(line,nList))
        vals.append(int(digit))
    return(vals)


# // TEST OUTPUT //

'''
values = calVals(test1a,dgts)
test_total = sum(values)

print(f'Part 1: Test total = {test_total}')

values = calVals(test1b,alln)
test_total = sum(values)

print(f'Part 2: Test total = {test_total}')
'''

# // PUZZLE OUTPUT //

values = calVals(day1,dgts)
total = sum(values)

print(f'Part 1: Puzzle total = {total}')


values = calVals(day1,alln)
total = sum(values)

print(f'Part 2: Puzzle total = {total}')

