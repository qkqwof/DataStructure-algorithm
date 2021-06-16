n = int(input())
c_list = list(map(int,input().split()))
m = max(c_list)

n_list = []
for i in c_list:
    n_list.append(i/m*100)
print(sum(n_list)/n)