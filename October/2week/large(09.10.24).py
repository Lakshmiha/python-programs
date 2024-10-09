a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
c=int(input("Enter third no:"))
if((a>b)|(a>c)):
    print(a,"is largest")
elif(b>c):
    print(b,"is largest")
else:
    print(c,"is largest")
