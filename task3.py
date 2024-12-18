#! python3
"""
##### Task 3
Print all the numbers from 1 to 1000 that are divisible by 5.
"""

for i in range(1001):
    jum = float(i/5)
    num = int(jum)
    tum = float(num)
    if jum == tum:
        print(i, end=' ')