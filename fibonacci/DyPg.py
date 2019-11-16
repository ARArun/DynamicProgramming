#!/usr/bin/python3

print('start')
'''
Recursion is very process intensive and time consuming

Dynamic Programming is Memory Intensive and not Process Intensive

'''

#Memoisation
memo = dict()
def fib(n):
    if n <= 1:
        memo[n] = n
        return n
    try:
        return memo[n]
    except KeyError:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]

print(fib(100))