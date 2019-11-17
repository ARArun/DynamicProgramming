#! /usr/bin/python3

'''
+ Tabulation works in Bottum Up approach
+ Reduces the function Calls, saves function call Over head time

'''

LookUp = dict()

def fib(n):
    LookUp[1] = 0
    LookUp[2] = 1
    for i in range(3, n+1):
        LookUp[i] = LookUp[i-1] + LookUp[i-2]
    return LookUp[n]

print(fib(100))