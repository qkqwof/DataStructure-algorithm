import sys
sys.stdin = open("input.txt","r")

n = int(input())
arr = []
arr = list(map(int,str(n)))
arr.sort(reverse=True)

for i in arr:
    print(i,end="")
