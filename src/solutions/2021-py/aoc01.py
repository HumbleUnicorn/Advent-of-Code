# Ruth Wertz
# AOC 2021 - Day 1
# https://adventofcode.com/2021/day/1


# //READ DATA//
test=[]
with open('t01.txt') as f: 
    for lines in f:
        test.append(lines)
test=[int(i) for i in test]

data=[]
with open('d01.txt') as f: 
    for lines in f:
        data.append(lines)
data=[int(i) for i in data]


#// RUN PART 1 WITH TEST DATA
test1=7
n=len(test)
i=0
s=0
while i<(n-1):
    a=test[i]
    b=test[i+1]
    if b>a :
        s=s+1
    i=i+1
if test1==s:
    print("TEST Part 1 ==> Passed")
else:
    print("TEST Part 1 ==> Nope")

#// RUN PART 1 WITH PUZZLE DATA
n=len(data)
i=0
s=0
while i<(n-1):
    a=data[i]
    b=data[i+1]
    if b>a :
        s=s+1
    i=i+1
print('SOLUTION PART 1:',s)


#// RUN PART 2 WITH TEST DATA //

#Write list of sums
test2=5
test_sums=[]
n=len(test)
i=0
while i<(n-2):
   a=[test[i],test[i+1],test[i+2]]
   A=sum(a)
   test_sums.append(A)        
   i=i+1

# Read list of sums
n=len(test_sums)
s=0
j=0
while j<(n-1):
    a=test_sums[j]
    b=test_sums[j+1]
    if b>a :
        s=s+1
    j=j+1
if test2==s:
    print("TEST Part 2 ==> Passed")
else:
    print("TEST Part 2 ==> Nope")


#// RUN PART 2 WITH PUZZLE DATA //

#Write list of sums
sums=[]
n=len(data)
i=0
while i<(n-2):
   a=[data[i],data[i+1],data[i+2]]
   A=sum(a)
   sums.append(A)        
   i=i+1
   
# Read list of sums
n=len(sums)
s=0
j=0
while j<(n-1):
    a=sums[j]
    b=sums[j+1]
    if b>a :
        s=s+1
    j=j+1
print('SOLUTION PART 2:',s)