import sys
sys.stdin = open("input.txt","r")

T = int(sys.stdin.readline())

for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)