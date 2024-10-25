s=['10','12','22','6']
res=map(int,s)
print(list(res))
sum=0
for i in s:
    sum=sum+int(i)
print("The sum of nos is:",sum)
