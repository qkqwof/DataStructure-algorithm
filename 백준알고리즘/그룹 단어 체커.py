import sys
sys.stdin = open("input.txt","r")

n = int(input())
cnt=n
for _ in range(n):
    str = input()
    for i in range(len(str)-1):
        if str.find(str[i]) > str.find(str[i+1]):
            cnt-=1
            break
print(cnt)