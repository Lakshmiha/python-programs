def fibo(i):
    if i<=1:
        return i;
    else:
        return (fibo(i-1)+fibo(i-2))
num=5
for i in range(num):
        print(fibo(i),end=" ")
    
    
