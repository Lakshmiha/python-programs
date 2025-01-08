str1=input("Enter a string:")
vow=["a","e","i","o","u"]
string=[]
for i in str1:
    if i in vow:
        string.append(i)
        
print("No of vowels:",len(string))

string1=str1
for i in vow:
    string1=string1.replace(i, "#")
print(string1)
