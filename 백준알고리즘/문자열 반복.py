import sys
sys.stdin = open("input.txt","r")

T = int(input())

for i in range(T):
    r,s = input().split()
    r = int(r)
    s = str(s)
    for j in range(len(s)):
        print(r*s[j], end="")
    print()


