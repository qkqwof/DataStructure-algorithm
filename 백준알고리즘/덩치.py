import sys
sys.stdin = open("input.txt","r")

n = int(input())

# 입력받은 정보를 저장할 리스트
d = [] 

# 등수정보를 저장할 리스트
result = []

# 변수 저장
for i in range(n):
    a, b = map(int,input().split())
    d.append((a,b)) # 몸무게와 키를 튜플 형태로 묶어줌

# 덩치
for i in range(n):
    count = 0
    for j in range(n):
        # 키와 몸무게 모두 자신보다 큰 사람의 수를 센다.
        if d[i][0] < d[j][0] and d[i][1] < d[j][1]:
            count += 1
    # 덩치 등수는 자신보다 몸무게 키 모두 큰 사람의 수 + 1 이므로 count + 1을 ans에 append한다.
    result.append(count + 1) 
    
for d in result:
    print(d,end=" ")
