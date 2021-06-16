# 함수 d 구현하기
def d(n):
    n=n+sum(map(int,str(n)))
    return n

# 생성자가 있는지 확인할 리스트 초기화하기
a = [0]*10001

# 생성자 찾기
for i in range(1,10001):
    a[i] = d(i)
    # 셀프넘버라면 출력하기
    if i not in a:
        print(i)