n,k=list(map(int,input().split(' ')))
a=list(map(int,input().split(' ')))
a=list(a)
count=0
for i in range(len(a)):
    if a[i] >= a[k-1] and a[i]>0:
        count=count+1
print(count)