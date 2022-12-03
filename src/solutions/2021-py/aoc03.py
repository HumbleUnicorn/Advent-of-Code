# Ruth Wertz
# AOC 2021 - Day 3
# https://adventofcode.com/2021/day/3

# //READ DATA//

test=[]
with open('C:/Users/ruthw/OneDrive/Documents/Side Quests/Advent-of-Code/inputs/2021/t03.txt') as f: 
    for lines in f:
        test.append(lines.split())
    for i in range(len(test)):
        test[i]=test[i][0]
#print(test)
#print(type(test),len(test))
#print(type(test[0]),len(test[0])) 
    

day3=[]
with open('C:/Users/ruthw/OneDrive/Documents/Side Quests/Advent-of-Code/inputs/2021/d03.txt') as f: 
    for lines in f:
        day3.append(lines.split()) 
    for i in range(len(day3)):
        day3[i]=day3[i][0] 
#print(day3)
#print(type(day3),len(day3))
#print(type(day3[0]),len(day3[0])) 
    

#// PART 1 BITFIND FUNCTION
def findBit(run_data):
    #Initial Values
    g=str()         
    e=str()        
    n=len(run_data)
    m=len(run_data[0])
    #Loop
    for j in range (m):
        a=0 #'0' counter
        b=0 #'1' counter
        for i in range(n): 
            if run_data[i][j] == '0':
                a+=1
            else: 
                b+=1
        if a>b:
            g=str(g+'0')
            e=str(e+'1')
        else:
            g=str(g+'1')
            e=str(e+'0')
    results = [g,int(g,2),e,int(e,2),int(g,2)*int(e,2)]
    return results


#// PART 1 RUN FUNCTION WITH TEST DATA
test1=['10110',22,'01001',9,198]
p = findBit(test)
if p == test1:
    print('Test1 ===> Successful')
else:
    print('Test1 ===> Nope, Try Again')


#// PART 1 RUN FUNCTION WITH PUZZLE DATA 
s = findBit(day3)
print('SOLUTION PART 1:',s[4])