num=int(input("Enter a no:"))
for i in range(0,num):
    for j in range(i):
        print("*",end=' ')
    print(' ')
for i in range(num,0,-1):
    for j in range(i):
        print("*",end=' ')
    print(' ')
