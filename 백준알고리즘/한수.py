#num = int(input())
#h_cnt = 0
#for i in range(1,num+1):
#    num_list = list(map(int,str(i)))
#    if i < 100:
#        h_cnt += 1 # 100보다 작으면 모두 한수
#    elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
#        h_cnt += 1 # x의 각 자리가 등차수열이면 한수
#print(h_cnt)

def h(a):
    cnt = 0
    for i in range(1,a+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            cnt += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            cnt += 1
    return cnt


a = int(input())
print(h(a))