# Example of using shell-wildcard style matching in list comprehensions

from fnmatch import fnmatchcase as match

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

a = [addr for addr in addresses if match(addr, '* ST')]
print(a)

b = [addr for addr in addresses if match(addr, '54[0-9][0-9] *CLARK*')]
print(b)

import os

filenames = os.listdir(r'C:\Users\bach\Downloads')
print(filenames)

# List comprehension - http://www.diveintopython3.net/comprehensions.html#listcomprehension
filter = [name for name in filenames if name.endswith(('.mp4', '.wmv'))]
print('\'filter\' = ', filter)

print(any(name.endswith('.wmv') for name in filenames))
