import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n):
    [x,y] = map(int,input().split())
    nums.append([x,y])

snums = sorted(nums)

for i in range(n):
    print(snums[i][0], snums[i][1])