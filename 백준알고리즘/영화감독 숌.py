import sys
sys.stdin = open("input.txt","r")

n = int(input())

num = 666
while n != 0:
    # 666이라는 문자열이 num 안에 있으면
    if '666' in str(num):
        n = n-1
        if n == 0:
            break
    num = num + 1
print(num)