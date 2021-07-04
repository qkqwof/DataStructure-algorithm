import sys
sys.stdin = open("input.txt","r")

# 입력값 받아오기
n,m = map(int,input().split())
board = []

for i in range(n):
    board.append(input())
re = []

