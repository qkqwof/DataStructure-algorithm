import sys
sys.stdin = open("input.txt","r")

s = input()
alpha = "abcdefghijklmnopqrstuvwxyz"

for i in alpha:
    if i in s:
        print(s.index(i),end=" ")
    else:
        print(-1,end= " ")
