limit=int(input("Enter a limit:"))
first=0
second=1
third=1
print("Fibonacci series upto",limit,"is:")
print(first,end='')
for i in range(0,limit):
    print(third,end='')
    third=first+second
    first=second
    second=third
