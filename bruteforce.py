from itertools import combinations_with_replacement as mag
a=list(map(int,input().split()))
b=int(input())
l=[]
for i in range(1,b+1):
    l.append(mag(a,i))
temp=[]
for i in l:
    for j in i:
        if sum(j)==b:
            temp.append(j)
print(temp)
print(temp[0])
