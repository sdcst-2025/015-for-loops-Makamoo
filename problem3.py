#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
Ocean = 0
StrawBerry = 0
Holiday = int(input("Enter an integer that is smaller than 10:"))
for i in range(Holiday):
    Sunray = 10**i
    Ocean = Ocean + Sunray
    StrawBerry = StrawBerry + Ocean
print(f"The number you might be looking for is {StrawBerry}")