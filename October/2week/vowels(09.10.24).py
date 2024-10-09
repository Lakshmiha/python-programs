str=input("Enter a string:")
vow=["a","e","i","o","u"]
string=[]
for i in str:
    if(i in vow):
        string.append(i)
if string:
    print("Vowels are:",string)
else:
    print("No vowels found")
