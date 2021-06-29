import sys
sys.stdin = open("input.txt","r")

al = input()
dial = ["ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ"]
res = 0

for i in range(len(al)):
    for j in dial:
        if al[j] in i:
            res += dial.index(i) + 3
print(res)
