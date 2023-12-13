import re

def find_consecutive_digits(text):
    matches = re.finditer(r'\d+', text)
    return [(match.group(), match.start(), match.end()) for match in matches]

text = "Hello123World456"
digits = find_consecutive_digits(text)
print(digits) # Output: [('123', 5, 8), ('456', 13, 16)]


def find_non_alphanumeric(text):
    # The pattern \W matches any non-alphanumeric character
    matches = re.finditer(r'\W', text)
    return [(match.group(), match.start()) for match in matches]

text = "Hello...W@rld...123"
symbols = find_non_alphanumeric(text)
for sym in symbols:
    if sym[0] != '.':
        print(sym[1])

print(symbols)  # Output: [(',', 5,), (' ', 6), (' ', 13), ('!', 18)]

start = 5
stop = 8
r = range(start, stop)

for i in r:
    print(i)  # Output: 5, 6, 7

xd = [0,1,2]
yd = [0]
xs = [2,3]
ys = []

import keyword

print(keyword.kwlist)
