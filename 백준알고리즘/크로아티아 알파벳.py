import sys
sys.stdin = open("input.txt","r")

a = ["c=","c-","dz=","d-","lj","nj","s=","z="]
alpha = input()

for i in a:
    alpha = alpha.replace(i,"a")
print(len(alpha))

# 개수를 셀 것이기 때문에 replace로 바꿔준다.
