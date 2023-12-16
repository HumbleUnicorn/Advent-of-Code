# # ============================================
# # find consecutive digits in a string

# import re

# def find_consecutive_digits(text):
#     matches = re.finditer(r'\d+', text); print(matches)
#     return [(match.group(), match.start(), match.end()) for match in matches]

# text = "Hello123World456"
# digits = find_consecutive_digits(text)
# print(digits) # Output: [('123', 5, 8), ('456', 13, 16)]

# # ============================================
# # find non-alphanumeric characters in a string

# import re

# def find_non_alphanumeric(text):
#     # The pattern \W matches any non-alphanumeric character
#     matches = re.finditer(r'\W', text)
#     return [(match.group(), match.start()) for match in matches]

# text = "Hello...W@rld...123"
# symbols = find_non_alphanumeric(text)
# for sym in symbols:
#     if sym[0] != '.':
#         print(sym[1])

# print(symbols)  # Output: [(',', 5,), (' ', 6), (' ', 13), ('!', 18)]

# # ============================================
# # check python keywords

# import keyword
# print(keyword.kwlist)

# # ============================================
# # find the common values between two lists

# from collections import Counter

# def find_common_values(list1, list2):
#     counter1 = Counter(list1)
#     counter2 = Counter(list2)
#     common = counter1 & counter2
#     return list(common.elements())

# set1 = [0, 1, 2, 4, 5]
# set2 = [2, 3, 4]
# common_values = find_common_values(set1, set2)
# print(common_values)  # Output: [2, 4]

# score = (len(common_values)) ** 2; print(score)

# # ============================================
# # create a dictionary from two lists

# test = [[50,98,2],[52,50,48]]
# src = []
# dst = []
# for line in test:
#     src += list(range(line[1],line[1]+line[2]))
#     dst += list(range(line[0],line[0]+line[2]))

# map1 = dict(zip(src, dst))
# print(map1) 

# # ============================================
# # check id a string contains a digit

# def contains_digits(s):
#     return any(character.isdigit() for character in s)

# s = "Hello123"
# print(contains_digits(s)) 

# # ============================================
# # convert a string to a list of integers

# str_list = ['1', '2', '3']
# int_list = list(map(int, str_list))
# print(int_list)  # Output: [1, 2, 3]

# seeds = '79 14 55 13'; print(type(seeds),seeds)
# seeds_str = seeds.split(' '); print(type(seeds_str),seeds_str)
# seeds_int = list(map(int, seeds_str))
# print(seeds_int)


# # ============================================
# # round float up to the nearest integer

# import math
# # print(9/7)
# # print(math.ceil(9/7))

# x=math.ceil(9/7)
# y=int(7/2)
# n=len(range(x,y+1))*2
# print(n)

# x=math.ceil(40/15)
# y=int(15/2)
# n=len(range(x,y+1))*2
# print(n)


# # ============================================
# # messing around with quadratic equations

import math

# coefficients
a = 1  # coefficient of x^2
b = -30  # coefficient of x
c = 200  # constant term

# calculate the discriminant
D = b**2 - 4*a*c; print(D)

# check if the discriminant is positive, negative, or zero
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(min(x1,x2))
elif D == 0:
    x = -b / (2*a)
    print(x)
else:
    realPart = -b / (2*a)
    imaginaryPart = math.sqrt(-D) / (2*a)
    print("The solutions are complex: ", realPart, " + i", imaginaryPart, " and ", realPart, " - i", imaginaryPart)
    
 