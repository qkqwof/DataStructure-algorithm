import sys
sys.stdin = open("input.txt","r")

t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    print(a+b)