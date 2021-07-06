import sys
sys.stdin = open("input.txt","r")

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

arr1 = sorted(arr)

for i in range(len(arr)):
    print(arr1[i])
