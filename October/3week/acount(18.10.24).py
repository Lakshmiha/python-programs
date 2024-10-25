names=["Alice","Amanda","Michael","Sarah","Anna"]
a_count=0
for name in names:
    a_count+=name.lower().count('a')
print("The letter 'a' appears",a_count,"times in the line")
