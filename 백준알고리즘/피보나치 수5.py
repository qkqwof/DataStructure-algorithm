import sys
sys.stdin = open("input.txt","r")

def number(x):
    if x == 0:
        return 0 
    elif x == 1:
        return 1
    else:
        return number(x-1) + number(x-2)


n = int(input())
print(number(n))
