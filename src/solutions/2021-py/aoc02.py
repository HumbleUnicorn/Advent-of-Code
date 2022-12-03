# Ruth Wertz
# AOC 2021 - Day 2
# https://adventofcode.com/2021/day/2

# Read Data
test=[]
with open('C:/Users/ruthw/OneDrive/Documents/Side Quests/Advent-of-Code/inputs/2021/t02.txt') as f: 
    for lines in f:
        test.append(lines.split())
        
day2=[]
with open('C:/Users/ruthw/OneDrive/Documents/Side Quests/Advent-of-Code/inputs/2021/d02.txt') as f: 
    for lines in f:
        day2.append(lines.split())

# //PART 1 POSITION FUNCTION
def position_part1(run_data):
    h=0
    d=0
    for x in (run_data):
        if x[0]=='forward':
            h=h+int(x[1])
        elif x[0]=='down':
            d=d+int(x[1])
        else:
            d=d-int(x[1])
    return h,d,h*d


#//RUN FUNCTION ON TEST DATA//
test1=[15, 10, 150]
run_data=test
p1=list(position_part1(run_data))
if p1==test1:
    print("TEST Part 1 ==> Passed",p1)
else:
    print("TEST Part 1 ==> Nope")


# //RUN FUNCIOTN ON PUZZLE DATA
run_data=day2
s1=list(position_part1(run_data))
print('PART 1 SOLUTION:',s1[2])


#PART 2 POSITION FUNCTION
def position_part2(run_data):
    a=0
    h=0
    d=0
    for x in (run_data):
        if x[0]=='up':
            a=a-int(x[1])
        elif x[0]=='down':
            a=a+int(x[1])
        else:
            h=h+int(x[1])
            d=d+a*int(x[1])
    return h,d,h*d


# //RUN FUNCTION ON TEST DATA
test2=[15, 60, 900]
run_data=test
p2=list(position_part2(run_data))
if p2==test2:
    print("TEST Part 2 ==> Passed",p2)
else:
    print("TEST Part 2 ==> Nope")


# //RUN FUNCIOTN ON PUZZLE DATA
run_data=day2
s2=list(position_part2(run_data))
print('PART 2 SOLUTION:',s2[2])


