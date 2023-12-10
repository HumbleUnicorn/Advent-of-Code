# Ruth Wertz
# AOC 2021 - Day 3
# https://adventofcode.com/2021/day/3

# //READ DATA//

test=[]
with open('t03.txt') as f: 
    for lines in f:
        test.append(lines.split())
    for i in range(len(test)):
        test[i]=test[i][0]
#print(test)
#print(type(test),len(test))
#print(type(test[0]),len(test[0])) 
    

day3=[]
with open('d03.txt') as f: 
    for lines in f:
        day3.append(lines.split()) 
    for i in range(len(day3)):
        day3[i]=day3[i][0] 
#print(day3)
#print(type(day3),len(day3))
#print(type(day3[0]),len(day3[0])) 
    

#// PART 1: DEFINE GAMMA AND EPSILON FUNCTION
def findGamEp(run_data):
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


#// PART 1: RUN findGamEp FUNCTION WITH TEST DATA
test1=['10110',22,'01001',9,198]
p1 = findGamEp(test)
if p1 == test1:
    print('Test1 ===> Successful')
else:
    print('Test1 ===> Nope, Try Again')


#// PART 1: RUN findGamEp FUNCTION WITH PUZZLE DATA 
s1 = findGamEp(day3)
print('SOLUTION PART 1:',s1[4])


#// PART 2: DEFINE OXEGENY GENERATOR RATING FUNCTION//
def findOGR(run_data):
    #Initial Values            
    m=len(run_data[0])
    n=len(run_data)
    #Loop
    for j in range (m):
        n=len(run_data)
        a=0 #'0' counter
        b=0 #'1' counter
        retain=[]
        for i in range(n): 
            if run_data[i][j] == '0':
                a+=1
            else: 
                b+=1
        for i in range(n):
            c=run_data[i][j]
            if a>b and c=='0':
                retain.append(run_data[i])
            elif b>a and c == '1':
                retain.append(run_data[i])
            elif a==b and c == '1':
                retain.append(run_data[i])
        if len(retain)>1:
            run_data=retain
        elif len(retain)==1:
            o=retain[0]
            results=[o,int(o,2)]
    return(results)   
    
#// PART 2: DEFINE CO2 SCRUBBER RATING FUNCTION//
def findCSR(run_data):
    #Initial Values            
    m=len(run_data[0])
    n=len(run_data)
    #Loop
    for j in range (m):
        n=len(run_data)
        a=0 #'0' counter
        b=0 #'1' counter
        retain=[]
        for i in range(n): 
            if run_data[i][j] == '0':
                a+=1
            else: 
                b+=1
        for i in range(n):
            c=run_data[i][j]
            if a<b and c=='0':
                retain.append(run_data[i])
            elif b<a and c == '1':
                retain.append(run_data[i])
            elif a==b and c == '0':
                retain.append(run_data[i])
        if len(retain)>1:
            run_data=retain
        elif len(retain)==1:
            o=retain[0]
            results=[o,int(o,2)]
    return(results)   

# //PART 2: RUN findOGR and findCSR WITH TEST DATA//
ogr_test=['10111',23]
csr_test=['01010',10]
test2=230
ogr=findOGR(test) 
csr=findCSR(test)  
p2=ogr[1]*csr[1]
if ogr==ogr_test:
    print('Test for OGR ===> Successful')
if csr==csr_test:
    print('Test for CSR ===> Successful')
if p2==test2:
    print('Test2 ===> Successful')
else:
    print('Test2 ===> Nope, Try Again')
    
# //PART 2: RUN findOGR and findCSR WITH PUZZLE DATA//
ogr=findOGR(day3) 
csr=findCSR(day3)  
s2=ogr[1]*csr[1]
print('SOLUTION PART 2:',s2)