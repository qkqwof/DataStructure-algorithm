import sys
sys.stdin = open("input.txt","r")

def factorial(x):
    result = 1
    if x > 1:
        return x * factorial(x-1)
    else:
        return result
n = int(input())

print(factorial(n))