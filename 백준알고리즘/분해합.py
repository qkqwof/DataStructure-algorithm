import sys
sys.stdin = open("input.txt","r")

n = int(input())
nsum = 0

for i in range(1,n+1):
    num_list = list(map(int,str(i)))
    nsum = i + sum(num_list)

    if nsum == n:
        print(i)
        break
    if i == n:
        print(0)